from fastapi import FastAPI
from app.routers import todo


def get_application() -> FastAPI:
    app = FastAPI(title="Todo API")
    app.include_router(todo.router)
    return app


app = get_application()
