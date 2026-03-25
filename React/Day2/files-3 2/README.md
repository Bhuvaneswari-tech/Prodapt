# TaskMaster Pro (Vite + React + TypeScript + json-server-auth)

## Features
- Landing page
- Register / Login (json-server-auth)
- Protected Dashboard route
- Navbar: Add Task, counts, Logout
- Tasks: Add, Edit, Delete, Mark Done/Todo
- json-server backend (port 5001)

## Tech
- Vite + React + TypeScript
- react-router-dom
- json-server + json-server-auth

## Setup

### 1) Install
```bash
npm install
```

### 2) Start backend + frontend together
```bash
npm run dev
```

- Frontend: http://localhost:5173
- Backend: http://localhost:5001

## API Endpoints

### Auth (json-server-auth)
- `POST /register` with `{ "email": "...", "password": "..." }`
- `POST /login` with `{ "email": "...", "password": "..." }`

Returns:
- `accessToken`
- `user`

### Tasks (Protected with Bearer token)
- `GET /tasks?userId=<id>`
- `POST /tasks`
- `PATCH /tasks/:id`
- `DELETE /tasks/:id`

## Data Model

### users
Created automatically by json-server-auth.

### tasks
Each task belongs to a user via `userId`.

Example task:
```json
{
  "id": 1,
  "title": "Finish assignment",
  "description": "React case study",
  "status": "todo",
  "createdAt": 1770000000000,
  "userId": 1
}
```

## Notes / Troubleshooting
- If you see 401 errors in the console, your token is missing/expired. Logout and login again.
- If port 5001 is busy, change `--port 5001` in `package.json` and update `API_BASE` in `src/api/http.ts`.