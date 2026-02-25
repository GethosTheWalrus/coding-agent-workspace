"""Application entry point for the FastAPI Todo API.

This module creates the FastAPI instance, includes the todo router, and
exposes the ``app`` object for ASGI servers (uvicorn) and for testing.
It also ensures that the database tables are created on startup.
"""

from fastapi import FastAPI

# Import the router from the todo module
from .routers.todo import router as todo_router

# Import database metadata creation function
from . import database


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
    # Include routers
    app.include_router(todo_router)

    @app.on_event("startup")
    def on_startup() -> None:
        """Create database tables on application startup.
        """
        # Ensure tables are created; the function in database module creates them.
        database._create_tables()

    return app


# The ASGI application instance used by uvicorn.
app = get_application()
