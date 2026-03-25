// A tiny in-browser "server" that intercepts fetch() calls to /api/*
//
// Features:
// - POST /api/auth/login
// - GET  /api/restaurants/:id/menu
// - POST /api/orders
// - GET  /api/orders/:id   (status changes over time)
//
import type { MenuItem } from "../state/menu/types";
import type { Order, OrderEvent, OrderStatus } from "../state/order/types";

type Json = Record<string, unknown>;

const MENU_BY_RESTAURANT: Record<string, MenuItem[]> = {
  "campus-bistro": [
    { id: "m1", name: "Veggie Wrap", priceCents: 799 },
    { id: "m2", name: "Chicken Bowl", priceCents: 999 },
    { id: "m3", name: "French Fries", priceCents: 349 },
    { id: "m4", name: "Iced Coffee", priceCents: 399 },
  ],
};

type StoredOrder = {
  order: Order;
  createdAt: number;
  events: OrderEvent[];
};

const ORDERS = new Map<string, StoredOrder>();

function sleep(ms: number) {
  return new Promise((r) => setTimeout(r, ms));
}

function randomId(prefix: string) {
  return `${prefix}_${Math.random().toString(16).slice(2)}_${Date.now()}`;
}

function statusForAge(ageMs: number): { status: OrderStatus; eta: number | null; event?: OrderEvent } {
  // simple timeline
  // 0-4s: accepted
  // 4-10s: preparing
  // 10-16s: out_for_delivery
  // 16s+: delivered
  if (ageMs < 4000) {
    return {
      status: "accepted",
      eta: 18,
      event: { id: randomId("evt"), type: "ORDER_ACCEPTED", at: Date.now(), note: "Kitchen confirmed." },
    };
  }
  if (ageMs < 10000) {
    return {
      status: "preparing",
      eta: 12,
      event: { id: randomId("evt"), type: "ORDER_PREPARING", at: Date.now(), note: "Cooking now." },
    };
  }
  if (ageMs < 16000) {
    return {
      status: "out_for_delivery",
      eta: 6,
      event: { id: randomId("evt"), type: "OUT_FOR_DELIVERY", at: Date.now(), note: "Courier picked up." },
    };
  }
  return {
    status: "delivered",
    eta: 0,
    event: { id: randomId("evt"), type: "DELIVERED", at: Date.now(), note: "Enjoy your meal!" },
  };
}

function jsonResponse(body: unknown, init?: ResponseInit) {
  return new Response(JSON.stringify(body), {
    status: 200,
    headers: { "Content-Type": "application/json" },
    ...init,
  });
}

function errorResponse(message: string, status = 400) {
  return jsonResponse({ message }, { status });
}

function parseUrl(url: string) {
  const u = new URL(url, window.location.origin);
  return { pathname: u.pathname, searchParams: u.searchParams };
}

export function installMockServer() {
  const originalFetch = window.fetch.bind(window);

  window.fetch = async (input: RequestInfo | URL, init?: RequestInit) => {
    const url = typeof input === "string" ? input : input.toString();

    if (!url.startsWith("/api/")) {
      return originalFetch(input, init);
    }

    // simulate latency
    await sleep(250);

    const method = (init?.method ?? "GET").toUpperCase();
    const { pathname } = parseUrl(url);

    // AUTH
    if (method === "POST" && pathname === "/api/auth/login") {
      const body = init?.body ? (JSON.parse(init.body as string) as Json) : {};
      const email = String(body.email ?? "");
      const password = String(body.password ?? "");

      if (!email.includes("@") || password.length < 4) {
        return errorResponse("Invalid credentials.", 401);
      }

      return jsonResponse({
        token: "demo-token",
        user: { id: "u1", name: "Campus Student", email },
      });
    }

    // MENU
    const menuMatch = pathname.match(/^\/api\/restaurants\/([^/]+)\/menu$/);
    if (method === "GET" && menuMatch) {
      const rid = menuMatch[1];
      const items = MENU_BY_RESTAURANT[rid];
      if (!items) return errorResponse("Restaurant not found.", 404);
      return jsonResponse({ restaurantId: rid, items });
    }

    // CREATE ORDER
    if (method === "POST" && pathname === "/api/orders") {
      const body = init?.body ? (JSON.parse(init.body as string) as Json) : {};
      const restaurantId = String(body.restaurantId ?? "");
      const items = Array.isArray(body.items) ? body.items : [];

      if (!restaurantId || items.length === 0) return errorResponse("Invalid order payload.", 400);

      const id = randomId("order");
      const createdAt = Date.now();

      const order: Order = {
        id,
        restaurantId,
        status: "accepted",
        etaMinutes: 18,
      };

      const firstEvent: OrderEvent = {
        id: randomId("evt"),
        type: "ORDER_ACCEPTED",
        at: createdAt,
        note: "Kitchen confirmed.",
      };

      ORDERS.set(id, { order, createdAt, events: [firstEvent] });

      return jsonResponse({ order, events: [firstEvent] });
    }

    // GET ORDER (polling)
    const orderMatch = pathname.match(/^\/api\/orders\/([^/]+)$/);
    if (method === "GET" && orderMatch) {
      const oid = orderMatch[1];
      const stored = ORDERS.get(oid);
      if (!stored) return errorResponse("Order not found.", 404);

      const age = Date.now() - stored.createdAt;
      const next = statusForAge(age);

      // emit event only when status changed
      const prevStatus = stored.order.status;
      stored.order.status = next.status;
      stored.order.etaMinutes = next.eta;

      if (next.event && next.status !== prevStatus) {
        stored.events.push(next.event);
      }

      return jsonResponse({ order: stored.order, events: stored.events });
    }

    return errorResponse(`No route for ${method} ${pathname}`, 404);
  };
}