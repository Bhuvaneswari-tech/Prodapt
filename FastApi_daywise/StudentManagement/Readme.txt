Student Management System - FastAPI
===================================

Overview
--------
This project is a Student Management System built using FastAPI, SQLAlchemy, and Alembic. It demonstrates a modular structure with models, schemas, repositories, services, and controllers for managing students and courses.

Project Structure
-----------------
- app/
  - main.py
  - models/
    - database.py
    - models.py
  - schemas/
    - schemas.py
  - repositories/
    - repository.py
  - services/
    - service.py
  - controllers/
    - student_controller.py
    - course_controller.py
- alembic/
  - env.py
  - versions/
- alembic.ini
- requirements.txt

Setup Instructions
------------------
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Initialize Alembic (if not already present):**
   ```bash
   alembic init alembic
   ```
   (This creates the alembic/ folder and alembic.ini. Already included in this project.)

3. **Configure Alembic:**
   - In `alembic.ini`, set the `sqlalchemy.url` to match your database (default is SQLite: `sqlite:///./student.db`).
   - In `alembic/env.py`, ensure your models are imported and `target_metadata` is set to `Base.metadata` from your models.

4. **Create a migration revision:**
   ```bash
   alembic revision --autogenerate -m "Initial migration"
   ```
   This generates a migration script in `alembic/versions/`.

5. **Apply migrations to the database:**
   ```bash
   alembic upgrade head
   ```

6. **Run the FastAPI server:**
   ```bash
   uvicorn app.main:app --reload
   ```

API Endpoints
-------------
- `/api/students/` - CRUD operations for students
- `/api/courses/` - CRUD operations for courses

Notes
-----
- Make sure to run migrations after modifying models.
- Use the service and repository layers for business logic and database access.
- Controllers (routers) handle API endpoints and dependency injection.

For more details, see the README.md in the project root.
