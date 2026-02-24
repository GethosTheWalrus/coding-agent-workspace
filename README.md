# Todo API

A simple **RESTful** Todo application built with **FastAPI** and **SQLite**.

## Features
- Create, read, update, and delete todo items
- SQLite database using SQLModel (SQLAlchemy + Pydantic)
- Automatic OpenAPI documentation (Swagger UI)

## Quick Start
```bash
# Clone the repo
git clone <repo-url>
cd <repo-dir>

# Install dependencies
pip install -r requirements.txt

# Run the development server
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. Swagger UI can be accessed at `http://127.0.0.1:8000/docs`.

## Project Structure
```
app/
├── __init__.py
├── main.py          # FastAPI entry point
├── models.py        # SQLModel definitions
├── crud.py          # Database operations
├── database.py      # Session & engine setup
└── routers/
    └── todo.py      # Todo endpoints

tests/
    test_todo.py     # Basic integration tests (to be added)
```

## License
MIT
