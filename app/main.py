"""FastAPI application entry point.

This module creates the FastAPI app instance, includes the API router,
and configures the database dependency.
"""

from fastapi import FastAPI
from app.api.v1.todo import router as todo_router

app = FastAPI(title="Todo API", version="0.1.0")

# Include the todo router under the /api/v1 prefix
app.include_router(todo_router, prefix="/api/v1")

# Root endpoint for health check
@app.get("/")
async def root():
    return {"message": "Todo API is running"}
