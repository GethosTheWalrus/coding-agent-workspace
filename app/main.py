from fastapi import FastAPI

from app.api import todo
from app.database import init_db


def create_app() -> FastAPI:
    """Create and configure the FastAPI application instance."""
    app = FastAPI(title="Todo API", version="0.1.0")
    app.include_router(todo.router, prefix="/todos", tags=["todos"])

    @app.on_event("startup")
    def on_startup():
        # Ensure all tables are created
        init_db()

    return app


app = create_app()
