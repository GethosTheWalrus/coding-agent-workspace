"""FastAPI application entry point.

Creates the FastAPI instance, includes routers, and configures the
application startup/shutdown events for the database.
"""

from fastapi import FastAPI
from .database import create_db_and_tables
from .routers import todo


def get_application() -> FastAPI:
    """Create and configure the FastAPI app.

    Returns
    -------
    FastAPI
        Configured FastAPI application instance.
    """
    app = FastAPI(title="Todo API", version="0.1.0")
    app.include_router(todo.router)
    return app


app = get_application()


@app.on_event("startup")
async def on_startup() -> None:
    """Create database tables on startup."""
    create_db_and_tables()

