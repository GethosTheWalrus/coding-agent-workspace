"""Application entry point for the FastAPI Todo service.

The `app` object is created here and includes the main router.
TODO: Add CORS middleware and include the todo router.
"""

from fastapi import FastAPI

app = FastAPI(title="Todo API")

# TODO: Include routers
# from .routers import todo
# app.include_router(todo.router)
