"""Application entry point for the FastAPI Todo service.

The `app` object is created here and includes the main router.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import todo
from .database import engine
from . import models

app = FastAPI(title="Todo API")

# Create database tables if they don't exist
models.Base.metadata.create_all(bind=engine)

# Set up CORS (allow all for simplicity)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(todo.router)
