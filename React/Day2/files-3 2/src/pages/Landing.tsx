import { Link } from "react-router-dom";

export default function Landing() {
  return (
    <div className="card">
      <h1>TaskMaster Pro</h1>
      <p className="muted">
        A Vite + React + TypeScript app using json-server-auth for authentication and a protected tasks API.
      </p>

      <div className="row">
        <Link className="btn" to="/login">Login</Link>
        <Link className="btn secondary" to="/register">Register</Link>
      </div>
    </div>
  );
}