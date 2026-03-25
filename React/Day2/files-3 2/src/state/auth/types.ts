export type User = {
  id: string;
  name: string;
  email: string;
};

export type AuthState = {
  status: "idle" | "loading" | "authenticated" | "error";
  isAuthenticated: boolean;
  user: User | null;
  token: string | null;
  error: string | null;
};