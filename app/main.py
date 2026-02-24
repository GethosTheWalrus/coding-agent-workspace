"""FastAPI application entry point.

This module creates the FastAPI app instance, includes the todo router,
and provides a function to start the server via `uvicorn`.
"""

from fastapi import FastAPI
from .routers import todo
from . import database


def get_app() -> FastAPI:
    """Create and configure the FastAPI application.

    Returns
    -------
    FastAPI
        Configured FastAPI instance with routers included.
    """
    app = FastAPI(title="Todo API", version="0.1.0")
    app.include_router(todo.router)

    @app.on_event("startup")
    def on_startup() -> None:
        """Create database tables when the application starts."""
        database.create_db_and_tables()

    return app


# When running `uvicorn app.main:app --reload`, FastAPI will look for a variable
# named `app`.  We expose it here for convenience.
app = get_app()
