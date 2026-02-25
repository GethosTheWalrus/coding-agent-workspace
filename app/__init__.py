"""FastAPI Todo application package.

This package contains the core FastAPI app, database models, Pydantic schemas,
CRUD utilities, and API routers.

The actual implementation of the business logic will be added by the
backend developer.
"""

# Export the FastAPI app instance for external tools (e.g., uvicorn)
from .main import app  # noqa: F401
