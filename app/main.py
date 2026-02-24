"""FastAPI application entry point.

The app is created here so that it can be imported by both the server
runtime (uvicorn) and the test suite without side‑effects.
"""

from fastapi import FastAPI
from .database import init_db
from .routers import todo


def create_app() -> FastAPI:
    """Create and configure a FastAPI instance.

    Returns
    -------
    FastAPI
        The configured FastAPI application with routes and database
        initialisation.
    """
    app = FastAPI(title="Todo API")
    # Include routers
    app.include_router(todo.router)
    # Initialise the database (creates tables if needed)
    @app.on_event("startup")
    async def on_startup() -> None:
        init_db()

    return app

# Export a ready‑to‑run app instance for uvicorn.
app = create_app()
