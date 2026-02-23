# Architecture Overview

## Goal
Create a **RESTful Todo API** using **FastAPI** with a **SQLite** backend. The API will expose endpoints to create, read, update, and delete todo items.

## Technology Stack
| Layer | Technology |
|-------|------------|
| Web Framework | **FastAPI** (Python 3.11) |
| ASGI Server | **uvicorn** |
| ORM / Database | **SQLAlchemy** (Core + ORM) |
| Database | **SQLite** (file‑based) |
| Data Validation | **Pydantic** (built‑in with FastAPI) |
| Dependency Management | **requirements.txt** |
| Testing | **pytest**, **httpx** |

## Directory Layout
```
project_root/
│   README.md
│   requirements.txt
│   .gitignore
│
├───app/                     # Core application package
│   │   __init__.py
│   │   main.py               # FastAPI entry point
│   │   database.py           # DB engine & session handling
│   │
│   ├───api/                 # API routers (FastAPI APIRouter objects)
│   │       __init__.py
│   │       todo.py           # CRUD endpoints for Todo model
│   │
│   ├───models/              # SQLAlchemy ORM models
│   │       __init__.py
│   │       todo.py
│   │
│   ├───schemas/             # Pydantic models for request/response
│   │       __init__.py
│   │       todo.py
│   │
│   └───crud/                # Business‑logic functions that interact with DB
│           __init__.py
│           todo.py
│
└───tests/                    # Automated tests (pytest)
        test_todo_api.py
```

## Data Model
**Todo**
- `id`: Integer, primary key, auto‑increment
- `title`: String, required, max length 200
- `description`: String, optional, max length 1000
- `completed`: Boolean, default `False`
- `created_at`: DateTime, default `datetime.utcnow`
- `updated_at`: DateTime, auto‑updated on modification

## Component Responsibilities
| Component | Responsibility |
|-----------|----------------|
| `app/main.py` | Create FastAPI instance, include routers, configure middleware. |
| `app/database.py` | Initialise SQLite engine, provide `SessionLocal` and `Base` for models. |
| `app/models/todo.py` | SQLAlchemy ORM definition of the `Todo` table. |
| `app/schemas/todo.py` | Pydantic models: `TodoCreate`, `TodoUpdate`, `TodoRead`. |
| `app/crud/todo.py` | Functions: `get_todo`, `get_todos`, `create_todo`, `update_todo`, `delete_todo`. |
| `app/api/todo.py` | FastAPI router exposing `/todos/` endpoints, using CRUD functions and dependency‑injected DB session. |
| `tests/` | Unit and integration tests covering all CRUD operations via the API. |

## Interaction Flow
1. **Request** hits an endpoint defined in `app/api/todo.py`.
2. FastAPI injects a DB session (`Depends(get_db)`).
3. The endpoint calls the appropriate function from `app/crud/todo.py`.
4. CRUD function interacts with the SQLAlchemy model (`app/models/todo.py`).
5. Results are returned as Pydantic schemas (`app/schemas/todo.py`) which FastAPI serialises to JSON.

## Error Handling & Validation
- Pydantic validates request bodies automatically.
- Custom HTTPException (404) when a Todo is not found.
- Global exception handler can be added later for unexpected errors.

## Extensibility
- Adding authentication (OAuth2/JWT) would involve a new `app/auth/` package and dependency injection.
- Switching to PostgreSQL only requires updating `DATABASE_URL` in `app/database.py` and installing the appropriate driver.

---
*Prepared by the System Architect for the FastAPI Todo API project.*
