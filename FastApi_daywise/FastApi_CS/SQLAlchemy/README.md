# FastAPI SQLAlchemy ORM Mastery

Job Portal

This project demonstrates mastery of Database & ORM concepts using FastAPI, SQLAlchemy 2.0, and Alembic for migrations.

## Topics Covered
- **SQL Basics**: SELECT, INSERT, UPDATE, DELETE
- **SQLAlchemy ORM**: Modern 2.0 patterns, models for jobs, users, applications, relationships, transactions, session management
- **Database Migrations**: Alembic for schema changes

## Project Structure
- `app/models.py`: SQLAlchemy models for User, Job, Application
- `app/database.py`: Database connection and session management
- `app/crud.py`: CRUD operations
- `app/main.py`: FastAPI app with endpoints
- `alembic/`: Alembic migration scripts
- `requirements.txt`: Dependencies

## Setup & Running Instructions
1. **Create a virtual environment and activate it:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Initialize Alembic (if not already done):**
   ```bash
   alembic init alembic
   ```
4. **Edit `alembic.ini` and `alembic/env.py`** to set the correct database URL and import your models' `Base`.
5. **Run Alembic migrations:**
   ```bash
   alembic upgrade head
   ```
6. **Start the FastAPI server:**
   ```bash
   uvicorn app.main:app --reload
   ```

## Alembic Migration Commands
- **Create a new migration after model changes:**
  ```bash
  alembic revision --autogenerate -m "Describe change"
  alembic upgrade head
  ```
- **Downgrade to a previous migration:**
  ```bash
  alembic downgrade -1
  ```

## File Upload Instructions
To upload a file using FastAPI, you can use the `/upload/` endpoint (if implemented):

1. **Example using `curl`:**
   ```bash
   curl -F "file=@path/to/yourfile.txt" http://127.0.0.1:8000/upload/
   ```
2. **Or use the Swagger UI:**
   - Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Find the `/upload/` endpoint and use the "Try it out" button to upload a file.

> **Note:** Make sure you have implemented the upload endpoint in your FastAPI app.

## Usage
- Access the API docs at `http://127.0.0.1:8000/docs`
- Use endpoints to create users, jobs, applications, and perform CRUD operations

## Migrations
- To create a new migration after model changes:
  ```bash
  alembic revision --autogenerate -m "Describe change"
  alembic upgrade head
  ```

---

This project is for educational purposes and demonstrates best practices for modern Python database development.