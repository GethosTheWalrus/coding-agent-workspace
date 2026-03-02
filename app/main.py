"""FastAPI application entry point."""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .database import init_db
from .routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup/shutdown events."""
    # Startup: Initialize the database
    init_db()
    yield
    # Shutdown: cleanup if needed


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.

    Returns:
        Configured FastAPI application instance
    """
    app = FastAPI(
        title=settings.app_name,
        description="A REST API for managing todo items",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan,
    )

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routes
    app.include_router(router)

    return app


# Create the application instance
app = create_app()


@app.get("/", tags=["root"])
def root() -> dict:
    """Root endpoint returning API information."""
    return {"name": settings.app_name, "version": "1.0.0", "docs": "/docs"}


@app.get("/health", tags=["health"])
def health_check() -> dict:
    """Health check endpoint."""
    return {"status": "healthy"}
