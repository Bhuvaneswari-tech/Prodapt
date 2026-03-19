# JOB PORTAL APPLICATION – ENTERPRISE ARCHITECTURE DOCUMENTATION

PROJECT OVERVIEW

The Job Portal Application is a backend system designed using FastAPI and SQLAlchemy, following an enterprise-level layered architecture. It enables users to register, recruiters to post jobs, and candidates to apply for jobs.

This project demonstrates clean architecture principles including separation of concerns, scalability, and maintainability.

---

CASE STUDY

Problem Statement:
Design a scalable job portal system where:

* Users can register and browse jobs
* Recruiters can post job openings
* Users can apply for jobs
* System handles data efficiently with proper layering

Real-world Scenario:
A company like Naukri or LinkedIn needs:

* Millions of users
* Thousands of job postings
* Efficient application tracking
* Clean separation between business logic and database

Solution:
We implement a layered architecture:
Controller → Service → Repository → Database

---

ARCHITECTURE OVERVIEW

1. CONTROLLER LAYER

   * Handles HTTP requests
   * Validates input/output
   * Calls service layer

2. SERVICE LAYER

   * Contains business logic
   * Processes rules and validations
   * Calls repository layer

3. REPOSITORY LAYER

   * Handles database operations
   * Uses SQLAlchemy ORM

4. MODEL LAYER

   * Defines database tables

5. SCHEMA LAYER

   * Defines request/response structure using Pydantic

6. CORE LAYER

   * Database connection
   * Configuration

7. MIDDLEWARE

   * Logging
   * Exception handling
   * CORS

---

SQLALCHEMY WORKFLOW

Step 1: Define Models
Models represent database tables.
Example:
class User(Base):
**tablename** = "users"

Step 2: Create Engine
engine = create_engine(DATABASE_URL)

Step 3: Create Session
SessionLocal = sessionmaker(bind=engine)

Step 4: Dependency Injection
get_db() provides DB session to APIs

Step 5: CRUD Operations
db.add()
db.commit()
db.query()

Step 6: ORM Mapping
Converts Python objects ↔ Database rows

---

APPLICATION WORKFLOW

USER REQUEST FLOW:

1. Client sends HTTP request
2. Controller receives request
3. Controller calls Service
4. Service applies business logic
5. Service calls Repository
6. Repository interacts with DB via SQLAlchemy
7. Response flows back to client

Example Flow (Create User):
Client → Controller → Service → Repository → DB → Response

LAYER-WISE WORKFLOW

1. MODEL

   * Defines tables
   * Example: User, Job, Application

2. SCHEMA

   * Input validation
   * Output formatting
   * Example: UserCreate, UserResponse

3. REPOSITORY

   * Direct DB interaction
   * Example:
     db.add(user)
     db.commit()

4. SERVICE

   * Business rules
   * Example:
     Check duplicate email
     Apply validations

5. CONTROLLER

   * API endpoints
   * Example:
     POST /users
     GET /jobs

---

DATABASE DESIGN

Tables:

1. Users

   * id
   * name
   * email

2. Jobs

   * id
   * title
   * description

3. Applications

   * id
   * user_id (FK)
   * job_id (FK)

Relationships:

* One user → Many applications
* One job → Many applications

---

MIDDLEWARE FUNCTIONALITY

1. Logging Middleware

   * Logs request time and response time

2. Exception Handler

   * Handles runtime errors
   * Returns structured response

3. CORS Middleware

   * Allows cross-origin requests

---

HOW TO RUN THE APPLICATION

Step 1: Create Virtual Environment

Mac/Linux:
python3 -m venv venv
source venv/bin/activate

Windows:
python -m venv venv
venv\Scripts\activate

---

Step 2: Install Dependencies

```
pip install -r requirements.txt
```

---

Step 3: Run Application

```
uvicorn main:app --reload
```

---

Step 4: Access Application

Browser:
http://127.0.0.1:8000

Swagger UI:
http://127.0.0.1:8000/docs

---

SAMPLE API ENDPOINTS

1. Create User
   POST /users/

2. Get Users
   GET /users/

3. Create Job
   POST /jobs/

4. Get Jobs
   GET /jobs/

5. Apply Job
   POST /applications/

---

SAMPLE REQUEST JSON

Create User:
{
"name": "John",
"email": "[john@example.com](mailto:john@example.com)"
}

Create Job:
{
"title": "Python Developer",
"description": "FastAPI + SQLAlchemy"
}

Apply Job:
{
"user_id": 1,
"job_id": 1
}

---
KEY FEATURES

* Clean Architecture
* Scalable Design
* SQLAlchemy ORM
* FastAPI Integration
* Middleware Support
* Modular Code Structure

---

BEST PRACTICES FOLLOWED

* Separation of Concerns
* Dependency Injection
* Reusable Components
* Maintainable Code
* Layered Design Pattern

---

FUTURE ENHANCEMENTS

* JWT Authentication
* Role-Based Access (Admin/User)
* Pagination & Filtering
* Docker Deployment
* Unit Testing (pytest)
* Alembic Migrations
* Async SQLAlchemy

---

CONCLUSION

This Job Portal Application demonstrates how to build a real-world scalable backend system using FastAPI and SQLAlchemy with enterprise architecture. It is suitable for production-level systems and can be extended easily with advanced features.

=================================================================
END OF DOCUMENT
===============
