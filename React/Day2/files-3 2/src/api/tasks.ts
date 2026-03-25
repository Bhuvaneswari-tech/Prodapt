import { apiFetch } from "./http";

export type Task = {
  id: number;
  title: string;
  description?: string;
  status: "todo" | "inprogress" | "done";
  createdAt: number;
  userId: number;
};

export type NewTask = Omit<Task, "id" | "createdAt">;

export async function fetchTasks(userId: number) {
  // restrict by userId (client-side filter query)
  return apiFetch<Task[]>(`/tasks?userId=${userId}`, { auth: true });
}

export async function createTask(task: NewTask) {
  return apiFetch<Task>("/tasks", { method: "POST", json: { ...task, createdAt: Date.now() }, auth: true });
}

export async function updateTask(id: number, patch: Partial<Task>) {
  return apiFetch<Task>(`/tasks/${id}`, { method: "PATCH", json: patch, auth: true });
}

export async function deleteTask(id: number) {
  await apiFetch<unknown>(`/tasks/${id}`, { method: "DELETE", auth: true });
}