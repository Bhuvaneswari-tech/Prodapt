import React, { createContext, useContext, useMemo, useReducer } from "react";
import type { MenuItem, MenuState } from "./types";
import { apiFetch } from "../../api/client";

type MenuAction =
  | { type: "FETCH_START"; restaurantId: string }
  | { type: "FETCH_SUCCESS"; restaurantId: string; items: MenuItem[]; fetchedAt: number }
  | { type: "FETCH_ERROR"; error: string }
  | { type: "INVALIDATE" };

const initialState: MenuState = {
  status: "idle",
  restaurantId: null,
  items: [],
  fetchedAt: null,
  error: null,
};

function reducer(state: MenuState, action: MenuAction): MenuState {
  switch (action.type) {
    case "FETCH_START":
      return { ...state, status: "loading", error: null, restaurantId: action.restaurantId };
    case "FETCH_SUCCESS":
      return {
        status: "success",
        restaurantId: action.restaurantId,
        items: action.items,
        fetchedAt: action.fetchedAt,
        error: null,
      };
    case "FETCH_ERROR":
      return { ...state, status: "error", error: action.error };
    case "INVALIDATE":
      return { ...initialState };
    default:
      return state;
  }
}

type MenuContextValue = {
  state: MenuState;
  actions: {
    fetchMenu: (restaurantId: string) => Promise<void>;
    invalidate: () => void;
  };
};

const MenuContext = createContext<MenuContextValue | null>(null);

const STALE_AFTER_MS = 3 * 60 * 1000;

export function MenuProvider({ children }: { children: React.ReactNode }) {
  const [state, dispatch] = useReducer(reducer, initialState);

  const actions = useMemo(
    () => ({
      async fetchMenu(restaurantId: string) {
        // tiny cache check
        if (
          state.status === "success" &&
          state.restaurantId === restaurantId &&
          state.fetchedAt &&
          Date.now() - state.fetchedAt < STALE_AFTER_MS
        ) {
          return;
        }

        dispatch({ type: "FETCH_START", restaurantId });
        try {
          const res = await apiFetch<{ restaurantId: string; items: MenuItem[] }>(
            `/api/restaurants/${restaurantId}/menu`
          );
          dispatch({
            type: "FETCH_SUCCESS",
            restaurantId,
            items: res.items,
            fetchedAt: Date.now(),
          });
        } catch (e) {
          dispatch({
            type: "FETCH_ERROR",
            error: e instanceof Error ? e.message : "Failed to fetch menu",
          });
        }
      },
      invalidate() {
        dispatch({ type: "INVALIDATE" });
      },
    }),
    // depend on cache-related state
    [state.status, state.restaurantId, state.fetchedAt]
  );

  const value = useMemo(() => ({ state, actions }), [state, actions]);
  return <MenuContext.Provider value={value}>{children}</MenuContext.Provider>;
}

export function useMenu() {
  const ctx = useContext(MenuContext);
  if (!ctx) throw new Error("useMenu must be used within MenuProvider");
  return ctx;
}