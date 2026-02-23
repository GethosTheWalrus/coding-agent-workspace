from fastapi import FastAPI

from app.api import todo


def create_app() -> FastAPI:
    """Create and configure the FastAPI application instance."""
    app = FastAPI(title="Todo API", version="0.1.0")
    app.include_router(todo.router, prefix="/todos", tags=["todos"])
    return app


app = create_app()
