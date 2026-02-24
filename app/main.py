"""Main entry point for the FastAPI Todo application.

This module creates the FastAPI instance, includes the API routers, and
initialises the database (creating tables if they do not exist).
"""

from fastapi import FastAPI
from app.db.base import engine, Base
from app.api.todo import router as todo_router

# Create all tables (SQLite will create the file automatically)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo API", version="0.1.0")

# Include routers
app.include_router(todo_router, prefix="/todos", tags=["todos"])

# Root endpoint for health check
@app.get("/", include_in_schema=False)
async def root() -> dict:
    return {"message": "Todo API is running"}
