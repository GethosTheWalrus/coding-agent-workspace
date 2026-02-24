# app/main.py
"""FastAPI application entry point.

Creates the FastAPI app instance, includes routers, and configures any
middleware or event handlers.
"""

from fastapi import FastAPI
from .routers import todo

app = FastAPI(title="Todo API", version="0.1.0")

# Include the Todo router
app.include_router(todo.router)
