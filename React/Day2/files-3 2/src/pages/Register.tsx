import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../auth/AuthContext";

export default function Register() {
  const auth = useAuth();
  const nav = useNavigate();

  const [email, setEmail] = useState("user1@example.com");
  const [password, setPassword] = useState("password");

  return (
    <div className="card">
      <h2>Register</h2>

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
          const ok = await auth.actions.register(email, password);
          if (ok) nav("/dashboard");
        }}
        disabled={auth.state.status === "loading"}
      >
        {auth.state.status === "loading" ? "Creating..." : "Create account"}
      </button>

      <p className="muted">
        Already have an account? <Link to="/login">Login</Link>
      </p>
    </div>
  );
}