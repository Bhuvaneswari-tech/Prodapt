import { useEffect, useMemo, useState } from "react";
import { useAuth } from "../auth/AuthContext";
import type { Task } from "../api/tasks";
import * as tasksApi from "../api/tasks";
import Navbar from "../components/Navbar";
import TaskForm from "../components/TaskForm";
import TaskList from "../components/TaskList";

export default function Dashboard() {
  const auth = useAuth();
  const userId = auth.state.user!.id;

  const [tasks, setTasks] = useState<Task[]>([]);
  const [status, setStatus] = useState<"idle" | "loading" | "error">("idle");
  const [error, setError] = useState<string | null>(null);

  const [editing, setEditing] = useState<Task | null>(null);

  const counts = useMemo(() => {
    const todo = tasks.filter((t) => t.status === "todo").length;
    const inprogress = tasks.filter((t) => t.status === "inprogress").length;
    const done = tasks.filter((t) => t.status === "done").length;
    return { todo, inprogress, done, total: tasks.length };
  }, [tasks]);

  async function load() {
    setStatus("loading");
    setError(null);
    try {
      const res = await tasksApi.fetchTasks(userId);
      setTasks(res.sort((a, b) => b.createdAt - a.createdAt));
      setStatus("idle");
    } catch (e) {
      setStatus("error");
      setError(e instanceof Error ? e.message : "Failed to fetch tasks");
    }
  }

  useEffect(() => {
    load();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div className="dashboard">
      <Navbar
        userEmail={auth.state.user?.email ?? ""}
        counts={counts}
        onLogout={() => auth.actions.logout()}
        onAdd={() => setEditing(null)}
      />

      <div className="grid2">
        <div className="card">
          <h2>{editing ? "Edit Task" : "Add Task"}</h2>
          <TaskForm
            key={editing?.id ?? "new"}
            initial={editing ?? undefined}
            onCancel={editing ? () => setEditing(null) : undefined}
            onSave={async (data) => {
              try {
                if (editing) {
                  const updated = await tasksApi.updateTask(editing.id, data);
                  setTasks((prev) => prev.map((t) => (t.id === updated.id ? updated : t)));
                  setEditing(null);
                } else {
                  const created = await tasksApi.createTask({
                    ...data,
                    userId
                  });
                  setTasks((prev) => [created, ...prev]);
                }
              } catch (e) {
                alert(e instanceof Error ? e.message : "Save failed");
              }
            }}
          />
        </div>

        <div className="card">
          <div className="row" style={{ justifyContent: "space-between" }}>
            <h2>Task List</h2>
            <button className="secondary" onClick={load} disabled={status === "loading"}>
              {status === "loading" ? "Refreshing..." : "Refresh"}
            </button>
          </div>

          {status === "error" && <p className="error">Error: {error}</p>}

          <TaskList
            tasks={tasks}
            onEdit={(t) => setEditing(t)}
            onDelete={async (t) => {
              const ok = confirm(`Delete "${t.title}"?`);
              if (!ok) return;
              try {
                await tasksApi.deleteTask(t.id);
                setTasks((prev) => prev.filter((x) => x.id !== t.id));
              } catch (e) {
                alert(e instanceof Error ? e.message : "Delete failed");
              }
            }}
            onToggleDone={async (t) => {
              const next = t.status === "done" ? "todo" : "done";
              try {
                const updated = await tasksApi.updateTask(t.id, { status: next });
                setTasks((prev) => prev.map((x) => (x.id === updated.id ? updated : x)));
              } catch (e) {
                alert(e instanceof Error ? e.message : "Update failed");
              }
            }}
          />
        </div>
      </div>
    </div>
  );
}