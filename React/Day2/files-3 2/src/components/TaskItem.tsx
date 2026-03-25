import type { Task } from "../api/tasks";

export default function TaskItem(props: {
  task: Task;
  onEdit: () => void;
  onDelete: () => void;
  onToggleDone: () => void;
}) {
  const t = props.task;

  return (
    <li className="task">
      <div>
        <div className="taskTitle">
          {t.title}{" "}
          <span className="pill small">
            {t.status}
          </span>
        </div>
        {t.description && <div className="muted">{t.description}</div>}
        <div className="muted small">
          Created: {new Date(t.createdAt).toLocaleString()}
        </div>
      </div>

      <div className="row">
        <button className="secondary" onClick={props.onToggleDone}>
          {t.status === "done" ? "Mark Todo" : "Mark Done"}
        </button>
        <button className="secondary" onClick={props.onEdit}>Edit</button>
        <button className="danger" onClick={props.onDelete}>Delete</button>
      </div>
    </li>
  );
}