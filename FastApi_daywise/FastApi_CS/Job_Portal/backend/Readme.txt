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

NGROK WEBHOOK TESTING SETUP

To test webhook requests from your local FastAPI backend using a public URL, follow these steps with ngrok:

Step 1: Install ngrok
- Download from https://ngrok.com/download
- Or install via Homebrew (Mac):
  brew install --cask ngrok

Step 2: Start Your Local Webhook Receiver
- Run your local server that will receive webhook requests (e.g., Flask, FastAPI, or use webhook.site for testing).
- Example: If your webhook receiver runs on port 5000, make sure it is running:  http://localhost:5000

Step 3: Expose Localhost with ngrok
- In a new terminal, run:
  ngrok http 5000
- ngrok will display a public URL like: https://abcd1234.ngrok.io

Step 4: Set the WEBHOOK_URL Environment Variable
- In the terminal where you run your FastAPI backend, set:
  export WEBHOOK_URL="https://abcd1234.ngrok.io"
- Replace the URL with your actual ngrok public URL.

Step 5: Start Your FastAPI Backend
- Run:
  uvicorn main:app --reload

Step 6: Trigger a Webhook Event
- Use the API (e.g., register a user) to trigger the webhook.
- Your local receiver (via ngrok) will receive the POST request from your FastAPI app.

---
TIPS
- Each time you restart ngrok, you get a new public URL. Update WEBHOOK_URL accordingly.
- You can use webhook.site as a receiver for quick testing if you don’t have a local server.
- Check ngrok dashboard for request logs and debugging.

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

Webhooks in this project are handled by the send_webhook function in backend/app/utils/webhook.py. Here’s how it works:

The function reads a WEBHOOK_URL from environment variables.
When called, it sends a POST request to that URL with a JSON payload containing an event
name and associated data.
If the webhook URL is not set or the request fails, it returns False.
Where it’s used:

In application_service.py: After a job application, it sends a "job_applied" event with application details.
In job_service.py: After a job is created, it sends a "job_created" event with job details.
In user_service.py: After a user registers, it sends a "user_registered" event with user info.
This allows external systems to be notified in real time when key actions occur in your app. If you want to use webhooks, set the WEBHOOK_URL environment variable to your desired endpoint.