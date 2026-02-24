# FastAPI Todo API

A simple Todo REST API built with **FastAPI** and **SQLite** using SQLAlchemy ORM.

## Features
- Create, read, update, and delete todo items.
- SQLite database for lightweight persistence.
- Pydantic models for request/response validation.
- Fully typed code with modern FastAPI patterns.

## Running the app
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API documentation is available at `http://127.0.0.1:8000/docs`.
