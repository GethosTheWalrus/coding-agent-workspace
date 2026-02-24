# app/main.py
"""FastAPI application entry point.

This module creates the FastAPI app instance, includes routers, and
configures any middleware or event handlers.

TODO: Add any required middleware (CORS, logging, etc.) and include the
Todo router from `app.routers.todo`.
"""

from fastapi import FastAPI

app = FastAPI(title="Todo API", version="0.1.0")

# TODO: Include routers
# from app.routers import todo
# app.include_router(todo.router)
