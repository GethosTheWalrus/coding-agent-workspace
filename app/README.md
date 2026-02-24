# Todo API

A FastAPI based REST service for managing Todo items.

## Project Structure
```
app/
├── __init__.py
├── main.py          # FastAPI entry point
├── models.py        # SQLAlchemy models
├── schemas.py       # Pydantic schemas
├── crud.py          # CRUD helper functions (TODO: implement)
├── database.py      # DB session handling (TODO: implement)
└── routers/
    └── todo.py      # API router for /todos (TODO: implement)

tests/
├── __init__.py
├── conftest.py      # Pytest fixtures (TODO: implement)
└── test_todo.py     # API tests (TODO: implement)

Dockerfile           # Backend container (TODO: finalize)
requirements.txt     # Python dependencies
```

## Quick Start (TODO)
1. Build the Docker image:
   ```bash
   docker build -t todo-backend .
   ```
2. Run with Docker‑Compose (see `docker-compose.yml`).
3. Access the API at `http://localhost:8000`.

## Development Notes (TODO)
- Use **SQLAlchemy** with SQLite for persistence.
- Use **Pydantic** models for request/response validation.
- Include **CORS** middleware to allow the frontend to call the API.
- Add **uvicorn** entrypoint in `main.py`.
- Write comprehensive tests in `tests/` to achieve >90% coverage.
