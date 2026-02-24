# Architecture Overview

This document describes the high‑level architecture of the Todo API project.

## Directory Layout
```
.
├─ app/                # FastAPI application package
│   ├─ __init__.py
│   ├─ main.py         # Application entry point
│   ├─ models.py       # SQLModel data models
│   ├─ database.py     # Database connection utilities
│   └─ routers/
│       └─ todo.py     # CRUD router for todo items
├─ tests/              # Pytest test suite
│   └─ test_todo.py
├─ .gitignore
├─ requirements.txt
├─ README.md
└─ docs/
    └─ architecture.md
```

## Technology Stack
- **FastAPI** – Web framework for building APIs.
- **SQLModel** – ORM built on top of SQLAlchemy, providing Pydantic models.
- **SQLite** – Lightweight file‑based relational database.
- **Pytest** – Testing framework.
- **Coverage.py** – Code‑coverage measurement.
- **GitHub Actions** – CI pipeline.

## Component Overview
- **app/main.py** – Creates the FastAPI instance, includes routers, and configures startup/shutdown events.
- **app/models.py** – Defines the `Todo` model (id, title, description, completed).
- **app/database.py** – Provides a `SessionLocal` factory and a function to create the SQLite DB file.
- **app/routers/todo.py** – Implements CRUD endpoints:
  - `POST /todos/` – Create a new todo.
  - `GET /todos/` – List all todos.
  - `GET /todos/{todo_id}` – Retrieve a single todo.
  - `PUT /todos/{todo_id}` – Update a todo.
  - `DELETE /todos/{todo_id}` – Delete a todo.
- **tests/** – Contains unit/integration tests using `httpx.AsyncClient` against the FastAPI app.

## Data Flow
1. **Request** arrives at FastAPI router.
2. Router calls **SQLModel** session to interact with the SQLite DB.
3. Responses are serialized to JSON using Pydantic models.

## Extensibility
- Additional routers can be added under `app/routers/` and included in `main.py`.
- Switching to a different DB (e.g., PostgreSQL) only requires updating the connection string in `database.py`.
