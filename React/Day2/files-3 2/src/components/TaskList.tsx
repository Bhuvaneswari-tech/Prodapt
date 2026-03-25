import type { Task } from "../api/tasks";
import TaskItem from "./TaskItem";

export default function TaskList(props: {
  tasks: Task[];
  onEdit: (t: Task) => void;
  onDelete: (t: Task) => void;
  onToggleDone: (t: Task) => void;
}) {
  if (props.tasks.length === 0) {
    return <p className="muted">No tasks yet. Add your first task.</p>;
  }

  return (
    <ul className="list">
      {props.tasks.map((t) => (
        <TaskItem
          key={t.id}
          task={t}
          onEdit={() => props.onEdit(t)}
          onDelete={() => props.onDelete(t)}
          onToggleDone={() => props.onToggleDone(t)}
        />
      ))}
    </ul>
  );
}