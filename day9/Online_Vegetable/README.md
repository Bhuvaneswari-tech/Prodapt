
# FastAPI + MongoDB Case Study

## Project Description
This project is a production-ready backend API for an online vegetable store, built with FastAPI and MongoDB. It demonstrates:
- Secure JWT authentication
- Role-Based Access Control (RBAC) for admin and user roles
- Modular, enterprise-grade folder structure
- Clean separation of models, schemas, repositories, services, and controllers
- Middleware for CORS, logging, and exception handling
- Docker support for easy deployment
- Example test cases and guidance for database migrations

The API allows user registration, product management, and order processing, with endpoints protected by role-based permissions. It is designed for extensibility, maintainability, and real-world use in modern Python web backends.

## Features
- FastAPI backend with MongoDB
- JWT authentication
- Role-Based Access Control (RBAC)
- Enterprise folder structure
- Modular models, schemas, repositories, services, controllers
- Middleware: CORS, logging, exception handling
- Core: database, config, logging
- Testing with pytest

## Folder Structure
```
app/
  models/
    order.py
    product.py
    user.py
  schemas/
    order_schema.py
    product_schema.py
    user_schema.py
  repositories/
    order_repository.py
    product_repository.py
    user_repository.py
  services/
    order_service.py
    product_service.py
    user_service.py
  controllers/
    order_controller.py
    product_controller.py
    user_controller.py
  middleware/
    cors.py
    exception.py
    logging.py
  core/
    auth.py
    config.py
    database.py
    dependencies.py
    logging.py (configuration)
  testing/
    test_order.py
    test_product.py
    test_user.py
main.py
requirements.txt
```

## Running the App

## RBAC (Role-Based Access Control)

- **Roles:**
  - `admin`: Can access all endpoints, including admin-only routes.
  - `user`: Can access user and general endpoints.

**Role Permissions Example:**
| Endpoint           | Method | Role Required |
|--------------------|--------|--------------|
| /users/register    | POST   | Public       |
| /users/me         | GET    | user/admin   |
| /users/admin      | GET    | admin        |
| /products/        | POST   | user/admin   |
| /products/{id}    | GET    | user/admin   |
| /orders/          | POST   | user/admin   |
| /orders/{id}      | GET    | user/admin   |

## API Endpoints & Sample Input

### Register User
**POST** `/users/register`
```json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "testpass"
}
```
**Response:**
```json
{
  "id": "<user_id>",
  "username": "testuser",
  "email": "test@example.com",
  "role": "user"
}
```

### Get Current User
**GET** `/users/me` (Requires Bearer JWT)

### Admin Only
**GET** `/users/admin` (Requires Bearer JWT, admin role)

### Create Product
**POST** `/products/`
```json
{
  "name": "Tomato",
  "price": 2.5,
  "stock": 100
}
```

### Get Product
**GET** `/products/{id}`

### Create Order
**POST** `/orders/`
```json
{
  "user_id": "<user_id>",
  "product_ids": ["<product_id>"],
  "total": 10.0
}
```

### Get Order
**GET** `/orders/{id}`

## Docker

### Build and Run with Docker

1. **Build the Docker image:**
  ```bash
  docker build -t fastapi-mongo-app .
  ```
2. **Run the Docker container:**
  ```bash
  docker run -d -p 8000:8000 \
    --env MONGODB_URI="mongodb://host.docker.internal:27017" \
    fastapi-mongo-app
  ```
  - Adjust `MONGODB_URI` as needed for your environment.
  - Access the API at [http://localhost:8000](http://localhost:8000)

---

## Alembic (Database Migrations)

> **Note:** Alembic is typically used for SQL databases. For MongoDB, you can use migration tools like [MongoEngine-migrate](https://github.com/MongoEngine/mongoengine-migrate) or [Mongo-Migrate](https://github.com/CodeYellowBV/mongo-migrate). If you use Alembic for SQL, follow these steps:

1. **Install Alembic:**
  ```bash
  pip install alembic
  ```
2. **Initialize Alembic in your project:**
  ```bash
  alembic init alembic
  ```
3. **Edit `alembic.ini` and `env.py`** to set your database URL and models.
4. **Create a migration:**
  ```bash
  alembic revision --autogenerate -m "Initial migration"
  ```
5. **Apply migrations:**
  ```bash
  alembic upgrade head
  ```

For MongoDB, see the documentation of your chosen migration tool for similar steps.

---

## Local Development
1. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
2. Start MongoDB locally or update the URI in `app/core/config.py`.
3. Run the app:
  ```bash
  uvicorn app.main:app --reload
  ```
4. Run tests:
  ```bash
  pytest app/testing
  ```
