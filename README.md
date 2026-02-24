# Todo API

A simple **FastAPI** based REST API for managing todo items. The API uses **SQLite** via **SQLModel** for persistence and includes full CRUD operations.

## Features
- Create, read, update, and delete todo items
- SQLite database (file‑based, no external DB required)
- Automated test suite with >90% coverage
- GitHub Actions CI that runs tests and enforces coverage

## Running locally
```bash
# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Documentation
FastAPI automatically provides interactive docs at:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
