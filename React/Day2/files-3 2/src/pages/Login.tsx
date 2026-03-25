import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../auth/AuthContext";

export default function Login() {
  const auth = useAuth();
  const nav = useNavigate();

  const [email, setEmail] = useState("user1@example.com");
  const [password, setPassword] = useState("password");

  return (
    <div className="card">
      <h2>Login</h2>

      <label className="label">
        Email
        <input value={email} onChange={(e) => setEmail(e.target.value)} />
      </label>

      <label className="label">
        Password
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      </label>

      {auth.state.error && <p className="error">Error: {auth.state.error}</p>}

      <button
        onClick={async () => {
          const ok = await auth.actions.login(email, password);
          if (ok) nav("/dashboard");
        }}
        disabled={auth.state.status === "loading"}
      >
        {auth.state.status === "loading" ? "Signing in..." : "Sign in"}
      </button>

      <p className="muted">
        No account? <Link to="/register">Register</Link>
      </p>
    </div>
  );
}