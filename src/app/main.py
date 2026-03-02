"""FastAPI application entry point."""
from contextlib import asynccontextmanager

from fastapi import FastAPI

from .config import settings
from .database import init_db
from .routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup/shutdown events."""
    # Startup: initialize database
    init_db()
    yield
    # Shutdown: cleanup if needed


def create_app() -> FastAPI:
    """Create and configure the FastAPI application.
    
    Returns:
        Configured FastAPI application instance
    """
    app = FastAPI(
        title=settings.app_name,
        description="A REST API for a todo application",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan
    )
    
    # Include routes
    app.include_router(router)
    
    return app


# Create the application instance
app = create_app()


@app.get("/", tags=["root"])
def read_root():
    """Root endpoint returning API information."""
    return {
        "name": settings.app_name,
        "version": "1.0.0",
        "docs": "/docs"
    }