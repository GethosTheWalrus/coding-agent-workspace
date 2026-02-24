from fastapi import FastAPI
from app.routers import todo
from app.db import Base, engine


def get_application() -> FastAPI:
    app = FastAPI(title="Todo API")
    app.include_router(todo.router)

    @app.on_event("startup")
    def on_startup():
        # Create tables if they don't exist
        Base.metadata.create_all(bind=engine)

    return app


app = get_application()
