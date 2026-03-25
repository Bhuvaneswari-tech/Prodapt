import React, { createContext, useContext, useMemo, useReducer } from "react";

type Toast = { id: string; message: string };

type UIState = {
  toasts: Toast[];
};

type UIAction =
  | { type: "TOAST_ADD"; toast: Toast }
  | { type: "TOAST_DISMISS"; id: string };

const initialState: UIState = {
  toasts: [],
};

function reducer(state: UIState, action: UIAction): UIState {
  switch (action.type) {
    case "TOAST_ADD":
      return { ...state, toasts: [action.toast, ...state.toasts].slice(0, 3) };
    case "TOAST_DISMISS":
      return { ...state, toasts: state.toasts.filter((t) => t.id !== action.id) };
    default:
      return state;
  }
}

type UIContextValue = {
  state: UIState;
  actions: {
    toast: (message: string) => void;
    dismissToast: (id: string) => void;
  };
};

const UIContext = createContext<UIContextValue | null>(null);

export function UIProvider({ children }: { children: React.ReactNode }) {
  const [state, dispatch] = useReducer(reducer, initialState);

  const actions = useMemo(
    () => ({
      toast(message: string) {
        const id = `${Date.now()}_${Math.random().toString(16).slice(2)}`;
        dispatch({ type: "TOAST_ADD", toast: { id, message } });
        // auto-dismiss
        setTimeout(() => dispatch({ type: "TOAST_DISMISS", id }), 3500);
      },
      dismissToast(id: string) {
        dispatch({ type: "TOAST_DISMISS", id });
      },
    }),
    []
  );

  const value = useMemo(() => ({ state, actions }), [state, actions]);
  return <UIContext.Provider value={value}>{children}</UIContext.Provider>;
}

export function useUI() {
  const ctx = useContext(UIContext);
  if (!ctx) throw new Error("useUI must be used within UIProvider");
  return ctx;
}