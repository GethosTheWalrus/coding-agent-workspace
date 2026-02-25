"""Application entry point for the FastAPI Todo API.

This module creates the FastAPI instance, includes the todo router, and
exposes the ``app`` object for ASGI servers (uvicorn) and for testing.

Implementation details (e.g., middleware, CORS) can be added later by the
backend developer.
"""

from fastapi import FastAPI

# Import the router from the todo module
from .routers.todo import router as todo_router


def get_application() -> FastAPI:
    """Create and configure the FastAPI application.

    Returns
    -------
    FastAPI
        Configured FastAPI instance with routers included.
    """
    app = FastAPI(
        title="Todo API",
        description="A simple Todo REST API built with FastAPI and SQLite.",
        version="0.1.0",
    )
    # TODO: Add any middleware (e.g., CORS) if needed.
    app.include_router(todo_router)
    return app


# The ASGI application instance used by uvicorn.
app = get_application()
