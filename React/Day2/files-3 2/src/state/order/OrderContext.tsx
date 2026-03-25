import React, { createContext, useContext, useEffect, useMemo, useReducer, useRef } from "react";
import type { Order, OrderEvent, OrderState } from "./types";
import { apiFetch } from "../../api/client";

type PlaceOrderPayload = {
  restaurantId: string;
  items: { menuItemId: string; qty: number }[];
};

type OrderAction =
  | { type: "PLACE_START" }
  | { type: "PLACE_SUCCESS"; order: Order; events: OrderEvent[] }
  | { type: "PLACE_ERROR"; error: string }
  | { type: "TRACK_UPDATE"; order: Order; events: OrderEvent[] }
  | { type: "RESET" };

const initialState: OrderState = {
  status: "idle",
  activeOrder: null,
  events: [],
  error: null,
};

function reducer(state: OrderState, action: OrderAction): OrderState {
  switch (action.type) {
    case "PLACE_START":
      return { ...state, status: "placing", error: null };
    case "PLACE_SUCCESS":
      return { status: "tracking", activeOrder: action.order, events: action.events, error: null };
    case "PLACE_ERROR":
      return { ...state, status: "error", error: action.error };
    case "TRACK_UPDATE":
      return { ...state, status: "tracking", activeOrder: action.order, events: action.events, error: null };
    case "RESET":
      return { ...initialState };
    default:
      return state;
  }
}

type OrderContextValue = {
  state: OrderState;
  actions: {
    placeOrder: (payload: PlaceOrderPayload) => Promise<boolean>;
    resetOrder: () => void;
  };
};

const OrderContext = createContext<OrderContextValue | null>(null);

export function OrderProvider({ children }: { children: React.ReactNode }) {
  const [state, dispatch] = useReducer(reducer, initialState);
  const pollTimer = useRef<number | null>(null);

  const actions = useMemo(
    () => ({
      async placeOrder(payload: PlaceOrderPayload) {
        dispatch({ type: "PLACE_START" });
        try {
          const res = await apiFetch<{ order: Order; events: OrderEvent[] }>("/api/orders", {
            method: "POST",
            json: payload,
          });
          dispatch({ type: "PLACE_SUCCESS", order: res.order, events: res.events });
          return true;
        } catch (e) {
          dispatch({
            type: "PLACE_ERROR",
            error: e instanceof Error ? e.message : "Failed to place order",
          });
          return false;
        }
      },
      resetOrder() {
        dispatch({ type: "RESET" });
      },
    }),
    []
  );

  // polling while tracking
  useEffect(() => {
    if (!state.activeOrder) return;

    const orderId = state.activeOrder.id;

    async function poll() {
      try {
        const res = await apiFetch<{ order: Order; events: OrderEvent[] }>(`/api/orders/${orderId}`);
        dispatch({ type: "TRACK_UPDATE", order: res.order, events: res.events });

        if (res.order.status === "delivered") {
          // stop polling after delivered
          if (pollTimer.current) window.clearInterval(pollTimer.current);
          pollTimer.current = null;
        }
      } catch (e) {
        // soft-fail: stop polling and show error state
        if (pollTimer.current) window.clearInterval(pollTimer.current);
        pollTimer.current = null;
        dispatch({
          type: "PLACE_ERROR",
          error: e instanceof Error ? e.message : "Tracking failed",
        });
      }
    }

    // immediate poll + interval
    poll();
    pollTimer.current = window.setInterval(poll, 2000);

    return () => {
      if (pollTimer.current) window.clearInterval(pollTimer.current);
      pollTimer.current = null;
    };
  }, [state.activeOrder?.id]);

  const value = useMemo(() => ({ state, actions }), [state, actions]);
  return <OrderContext.Provider value={value}>{children}</OrderContext.Provider>;
}

export function useOrder() {
  const ctx = useContext(OrderContext);
  if (!ctx) throw new Error("useOrder must be used within OrderProvider");
  return ctx;
}