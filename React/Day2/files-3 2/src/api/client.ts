export async function apiFetch<T>(
  path: string,
  init?: RequestInit & { json?: unknown; token?: string | null }
): Promise<T> {
  const headers = new Headers(init?.headers);

  if (init?.json !== undefined) {
    headers.set("Content-Type", "application/json");
  }
  if (init?.token) {
    headers.set("Authorization", `Bearer ${init.token}`);
  }

  const res = await fetch(path, {
    ...init,
    headers,
    body: init?.json !== undefined ? JSON.stringify(init.json) : init?.body,
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