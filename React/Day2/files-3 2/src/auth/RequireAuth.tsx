import { Navigate, Outlet } from "react-router-dom";
import { useAuth } from "./AuthContext";

export function RequireAuth() {
  const auth = useAuth();
  if (!auth.state.user || !auth.state.token) {
    return <Navigate to="/login" replace />;
  }
  return <Outlet />;
}