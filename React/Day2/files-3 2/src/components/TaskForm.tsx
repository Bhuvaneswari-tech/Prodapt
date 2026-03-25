import { useState } from "react";
import type { Task } from "../api/tasks";

type FormData = Pick<Task, "title" | "description" | "status">;

export default function TaskForm(props: {
  initial?: Task;
  onSave: (data: FormData) => Promise<void>;
  onCancel?: () => void;
}) {
  const [title, setTitle] = useState(props.initial?.title ?? "");
  const [description, setDescription] = useState(props.initial?.description ?? "");
  const [status, setStatus] = useState<FormData["status"]>(props.initial?.status ?? "todo");
  const [saving, setSaving] = useState(false);

  return (
    <form
      onSubmit={async (e) => {
        e.preventDefault();
        if (!title.trim()) {
          alert("Title is required");
          return;
        }
        setSaving(true);
        try {
          await props.onSave({ title: title.trim(), description: description.trim(), status });
          if (!props.initial) {
            setTitle("");
            setDescription("");
            setStatus("todo");
          }
        } finally {
          setSaving(false);
        }
      }}
      className="form"
    >
      <label className="label">
        Title
        <input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="e.g., Finish assignment" />
      </label>

      <label className="label">
        Description
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Optional details"
          className="textarea"
        />
      </label>

      <label className="label">
        Status
        <select value={status} onChange={(e) => setStatus(e.target.value as FormData["status"])}>
          <option value="todo">Todo</option>
          <option value="inprogress">In progress</option>
          <option value="done">Done</option>
        </select>
      </label>

      <div className="row">
        <button type="submit" disabled={saving}>
          {saving ? "Saving..." : props.initial ? "Update" : "Add"}
        </button>
        {props.onCancel && (
          <button type="button" className="secondary" onClick={props.onCancel} disabled={saving}>
            Cancel
          </button>
        )}
      </div>
    </form>
  );
}