import React, { createContext, useContext, useMemo, useReducer } from "react";
import type { CartItem, CartState } from "./types";
import type { MenuItem } from "../menu/types";

type CartAction =
  | { type: "ADD_ITEM"; item: MenuItem; qty: number }
  | { type: "REMOVE_ITEM"; id: string }
  | { type: "UPDATE_QTY"; id: string; qty: number }
  | { type: "CLEAR" };

const initialState: CartState = {
  items: [],
  subtotalCents: 0,
};

function computeSubtotal(items: CartItem[]) {
  return items.reduce((sum, ci) => sum + ci.item.priceCents * ci.qty, 0);
}

function reducer(state: CartState, action: CartAction): CartState {
  switch (action.type) {
    case "ADD_ITEM": {
      const existing = state.items.find((x) => x.item.id === action.item.id);
      const items = existing
        ? state.items.map((x) =>
            x.item.id === action.item.id ? { ...x, qty: x.qty + action.qty } : x
          )
        : [...state.items, { item: action.item, qty: action.qty }];

      return { items, subtotalCents: computeSubtotal(items) };
    }
    case "REMOVE_ITEM": {
      const items = state.items.filter((x) => x.item.id !== action.id);
      return { items, subtotalCents: computeSubtotal(items) };
    }
    case "UPDATE_QTY": {
      const items = state.items
        .map((x) => (x.item.id === action.id ? { ...x, qty: action.qty } : x))
        .filter((x) => x.qty > 0);
      return { items, subtotalCents: computeSubtotal(items) };
    }
    case "CLEAR":
      return { ...initialState };
    default:
      return state;
  }
}

type CartContextValue = {
  state: CartState;
  actions: {
    addItem: (item: MenuItem, qty: number) => void;
    removeItem: (id: string) => void;
    updateQty: (id: string, qty: number) => void;
    clear: () => void;
  };
};

const CartContext = createContext<CartContextValue | null>(null);

export function CartProvider({ children }: { children: React.ReactNode }) {
  const [state, dispatch] = useReducer(reducer, initialState);

  const actions = useMemo(
    () => ({
      addItem(item: MenuItem, qty: number) {
        dispatch({ type: "ADD_ITEM", item, qty });
      },
      removeItem(id: string) {
        dispatch({ type: "REMOVE_ITEM", id });
      },
      updateQty(id: string, qty: number) {
        dispatch({ type: "UPDATE_QTY", id, qty });
      },
      clear() {
        dispatch({ type: "CLEAR" });
      },
    }),
    []
  );

  const value = useMemo(() => ({ state, actions }), [state, actions]);
  return <CartContext.Provider value={value}>{children}</CartContext.Provider>;
}

export function useCart() {
  const ctx = useContext(CartContext);
  if (!ctx) throw new Error("useCart must be used within CartProvider");
  return ctx;
}