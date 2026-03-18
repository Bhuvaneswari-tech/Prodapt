# Ecommerce FastAPI Project

## Features
- Category, Customer, Order, Product CRUD APIs
- MongoDB integration
- CORS and exception middleware

## Setup
1. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up MongoDB and update `.env` if needed.
4. Run the app:
   ```bash
   uvicorn app.main:app --reload
   ```

## Folder Structure
- app/models: Pydantic models
- app/schemas: Request/response schemas
- app/repositories: MongoDB access
- app/services: Business logic
- app/controllers: API routes
- app/middleware: CORS, exception handling
- app/core: Config, database connection

## .env Example
```
MONGODB_URL=mongodb://localhost:27017
MONGODB_DB_NAME=ecommerce_db
```
