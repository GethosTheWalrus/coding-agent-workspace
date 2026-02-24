from fastapi import FastAPI

from .routers import todo
from . import database


def get_application() -> FastAPI:
    app = FastAPI(title="Todo API")
    app.include_router(todo.router)

    @app.on_event("startup")
    def on_startup():
        # Ensure database tables are created at startup
        database.create_db_and_tables()

    return app


app = get_application()
