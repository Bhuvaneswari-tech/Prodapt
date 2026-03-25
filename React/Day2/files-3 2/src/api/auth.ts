import { apiFetch, setToken } from "./http";

export type AuthUser = {
  id: number;
  email: string;
};

export type LoginResponse = {
  accessToken: string;
  user: AuthUser;
};

export async function register(email: string, password: string) {
  // json-server-auth endpoint
  const res = await apiFetch<LoginResponse>("/register", {
    method: "POST",
    json: { email, password }
  });
  setToken(res.accessToken);
  localStorage.setItem("tm_user", JSON.stringify(res.user));
  return res;
}

export async function login(email: string, password: string) {
  // json-server-auth endpoint
  const res = await apiFetch<LoginResponse>("/login", {
    method: "POST",
    json: { email, password }
  });
  setToken(res.accessToken);
  localStorage.setItem("tm_user", JSON.stringify(res.user));
  return res;
}