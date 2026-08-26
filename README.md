# Patient Management API

A RESTful Patient Management API built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **Pydantic**.

This project demonstrates the fundamentals of backend API development, including CRUD operations, request/response validation, database integration, dependency injection, custom validation, and automatic API documentation.

## Features

- Create patient records
- Retrieve all patients
- Retrieve a patient by ID
- Update patient information
- Delete patient records
- PostgreSQL database integration
- SQLAlchemy ORM
- Pydantic request and response validation
- Custom email domain validation
- FastAPI dependency injection
- HTTP exception handling
- Automatic Swagger/OpenAPI documentation

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn
- Swagger / OpenAPI

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/GET/greet` | Returns a welcome message |
| GET | `/GET/get` | Retrieves all patients |
| GET | `/GET/get/{id}` | Retrieves a patient by ID |
| POST | `/CREATE/create` | Creates a new patient |
| PUT | `/UPDATE/update/{id}` | Updates patient information |
| DELETE | `/DELETE/delete/{id}` | Deletes a patient |

## Validation

The API uses Pydantic for request validation.

Email addresses are validated using:

- `EmailStr`
- Custom email-domain validation

Currently supported email domains:

- Gmail
- Yahoo

Invalid email domains are rejected with a validation error.

## Project Structure

```text
Patient Management System/
│
├── Database/
│   ├── __init__.py
│   ├── database_engine.py
│   └── database_models.py
│
├── Delete_Router/
│   ├── __init__.py
│   └── delete.py
│
├── Get_Router/
│   ├── __init__.py
│   └── get.py
│
├── Post_Router/
│   ├── __init__.py
│   └── post.py
│
├── Put_router/
│   ├── __init__.py
│   └── put.py
│
├── Pydantic/
│   ├── __init__.py
│   └── models.py
│
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
