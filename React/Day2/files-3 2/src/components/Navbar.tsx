import { useNavigate } from "react-router-dom";

export default function Navbar(props: {
  userEmail: string;
  counts: { todo: number; inprogress: number; done: number; total: number };
  onAdd: () => void;
  onLogout: () => void;
}) {
  const nav = useNavigate();

  return (
    <div className="nav">
      <div>
        <div className="brand" onClick={() => nav("/dashboard")} role="button" tabIndex={0}>
          TaskMaster Pro
        </div>
        <div className="muted small">Signed in as {props.userEmail}</div>
      </div>

      <div className="row">
        <span className="pill">Total: {props.counts.total}</span>
        <span className="pill">Todo: {props.counts.todo}</span>
        <span className="pill">In progress: {props.counts.inprogress}</span>
        <span className="pill">Done: {props.counts.done}</span>
      </div>

      <div className="row">
        <button onClick={props.onAdd}>Add Task</button>
        <button
          className="secondary"
          onClick={() => {
            props.onLogout();
            nav("/");
          }}
        >
          Logout
        </button>
      </div>
    </div>
  );
}