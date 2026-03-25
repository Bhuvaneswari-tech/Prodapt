import React, { createContext, useContext, useMemo, useReducer } from "react";
import type { AuthState, User } from "./types";
import { apiFetch } from "../../api/client";

type AuthAction =
  | { type: "LOGIN_START" }
  | { type: "LOGIN_SUCCESS"; user: User; token: string }
  | { type: "LOGIN_ERROR"; error: string }
  | { type: "LOGOUT" };

const initialState: AuthState = {
  status: "idle",
  isAuthenticated: false,
  user: null,
  token: null,
  error: null,
};

function reducer(state: AuthState, action: AuthAction): AuthState {
  switch (action.type) {
    case "LOGIN_START":
      return { ...state, status: "loading", error: null };
    case "LOGIN_SUCCESS":
      return {
        status: "authenticated",
        isAuthenticated: true,
        user: action.user,
        token: action.token,
        error: null,
      };
    case "LOGIN_ERROR":
      return { ...initialState, status: "error", error: action.error };
    case "LOGOUT":
      return { ...initialState };
    default:
      return state;
  }
}

type AuthContextValue = {
  state: AuthState;
  actions: {
    login: (email: string, password: string) => Promise<boolean>;
    logout: () => void;
  };
};

const AuthContext = createContext<AuthContextValue | null>(null);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [state, dispatch] = useReducer(reducer, initialState);

  const actions = useMemo(
    () => ({
      async login(email: string, password: string) {
        dispatch({ type: "LOGIN_START" });
        try {
          const res = await apiFetch<{ token: string; user: User }>("/api/auth/login", {
            method: "POST",
            json: { email, password },
          });
          dispatch({ type: "LOGIN_SUCCESS", token: res.token, user: res.user });
          return true;
        } catch (e) {
          dispatch({ type: "LOGIN_ERROR", error: e instanceof Error ? e.message : "Login failed" });
          return false;
        }
      },
      logout() {
        dispatch({ type: "LOGOUT" });
      },
    }),
    []
  );

  const value = useMemo(() => ({ state, actions }), [state, actions]);
  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used within AuthProvider");
  return ctx;
}