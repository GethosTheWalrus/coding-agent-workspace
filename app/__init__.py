# app/__init__.py
"""Top-level package for the Todo FastAPI application.

The package is intentionally lightweight; its primary purpose is to expose
the `app` object defined in :pymod:`app.main` when the package is imported.
"""

from .main import app  # noqa: F401
