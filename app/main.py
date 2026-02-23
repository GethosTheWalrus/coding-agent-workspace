"""FastAPI application entry point.

The ``app`` object is created here and the Todo router is included. When
running with ``uvicorn app.main:app`` the server will start and expose the
CRUD endpoints defined in ``app/routers/todo.py``.
"""

from __future__ import annotations

from fastapi import FastAPI

from .routers import todo

app = FastAPI(
    title="Todo API",
    description="A simple RESTful Todo service built with FastAPI and SQLite.",
    version="0.1.0",
)

# Include the Todo router.
app.include_router(todo.router)

# Create the database tables on startup if they do not exist.
@app.on_event("startup")
async def on_startup():
    from .database import engine, Base
    # Ensure all tables are created.
    Base.metadata.create_all(bind=engine)
