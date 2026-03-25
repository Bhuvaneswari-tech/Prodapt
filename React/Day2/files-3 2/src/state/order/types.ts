export type OrderStatus = "accepted" | "preparing" | "out_for_delivery" | "delivered";

export type Order = {
  id: string;
  restaurantId: string;
  status: OrderStatus;
  etaMinutes: number | null;
};

export type OrderEventType = "ORDER_ACCEPTED" | "ORDER_PREPARING" | "OUT_FOR_DELIVERY" | "DELIVERED";

export type OrderEvent = {
  id: string;
  type: OrderEventType;
  at: number;
  note?: string;
};

export type OrderState = {
  status: "idle" | "placing" | "tracking" | "error";
  activeOrder: Order | null;
  events: OrderEvent[];
  error: string | null;
};