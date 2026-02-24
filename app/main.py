# app/main.py
"""FastAPI application entry point.

This module creates the FastAPI instance, includes the Todo router, and
ensures that the SQLite database tables are created on startup.
"""

from fastapi import FastAPI
from .database import engine, create_db_and_tables
from .routers import todo

app = FastAPI(title="Todo API", version="0.1.0")

# Include the Todo router under the "/todos" prefix.
app.include_router(todo.router, prefix="/todos", tags=["todos"])

# Create database tables when the application starts.
@app.on_event("startup")
async def on_startup() -> None:
    """Create database tables if they do not exist.

    The function is async to match FastAPI's event handling model, but the
    underlying SQLModel call is synchronous and therefore runs in the event
    loop without blocking.
    """
    create_db_and_tables()
