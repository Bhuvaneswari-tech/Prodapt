import React, { createContext, useContext, useMemo, useState } from "react";
import * as authApi from "../api/auth";
import { clearToken } from "../api/http";

type AuthState = {
  user: authApi.AuthUser | null;
  token: string | null;
  status: "idle" | "loading" | "error";
  error: string | null;
};

type AuthContextValue = {
  state: AuthState;
  actions: {
    login: (email: string, password: string) => Promise<boolean>;
    register: (email: string, password: string) => Promise<boolean>;
    logout: () => void;
  };
};

const AuthContext = createContext<AuthContextValue | null>(null);

function loadUser(): authApi.AuthUser | null {
  const raw = localStorage.getItem("tm_user");
  if (!raw) return null;
  try {
    return JSON.parse(raw) as authApi.AuthUser;
  } catch {
    return null;
  }
}

function loadToken(): string | null {
  return localStorage.getItem("tm_token");
}

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [state, setState] = useState<AuthState>({
    user: loadUser(),
    token: loadToken(),
    status: "idle",
    error: null
  });

  const actions = useMemo(
    () => ({
      async login(email: string, password: string) {
        setState((s) => ({ ...s, status: "loading", error: null }));
        try {
          const res = await authApi.login(email, password);
          setState({ user: res.user, token: res.accessToken, status: "idle", error: null });
          return true;
        } catch (e) {
          setState((s) => ({
            ...s,
            status: "error",
            error: e instanceof Error ? e.message : "Login failed"
          }));
          return false;
        }
      },
      async register(email: string, password: string) {
        setState((s) => ({ ...s, status: "loading", error: null }));
        try {
          const res = await authApi.register(email, password);
          setState({ user: res.user, token: res.accessToken, status: "idle", error: null });
          return true;
        } catch (e) {
          setState((s) => ({
            ...s,
            status: "error",
            error: e instanceof Error ? e.message : "Register failed"
          }));
          return false;
        }
      },
      logout() {
        clearToken();
        setState({ user: null, token: null, status: "idle", error: null });
      }
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