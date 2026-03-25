export const API_BASE = "http://localhost:5001";

export type ApiError = { message: string };

export function getToken(): string | null {
  return localStorage.getItem("tm_token");
}

export function setToken(token: string) {
  localStorage.setItem("tm_token", token);
}

export function clearToken() {
  localStorage.removeItem("tm_token");
  localStorage.removeItem("tm_user");
}

export async function apiFetch<T>(
  path: string,
  init?: RequestInit & { json?: unknown; auth?: boolean }
): Promise<T> {
  const headers = new Headers(init?.headers);

  if (init?.json !== undefined) headers.set("Content-Type", "application/json");

  if (init?.auth) {
    const token = getToken();
    if (token) headers.set("Authorization", `Bearer ${token}`);
  }

  const res = await fetch(`${API_BASE}${path}`, {
    ...init,
    headers,
    body: init?.json !== undefined ? JSON.stringify(init.json) : init?.body
  });

  const text = await res.text();
  const data = text ? (JSON.parse(text) as unknown) : null;

  if (!res.ok) {
    const message =
      (data && typeof data === "object" && "message" in data && String((data as any).message)) ||
      `Request failed (${res.status})`;
    throw new Error(message);
  }

  return data as T;
}