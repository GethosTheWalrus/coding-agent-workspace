"""Database configuration for the FastAPI Todo API.

Uses a temporary file‑based SQLite database located in the system's temporary
directory. This avoids permission issues that can arise when writing to the
project root in the sandboxed execution environment.
"""

import os
import tempfile
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Determine a writable temporary directory.
_temp_dir = Path(tempfile.gettempdir())
_db_path = _temp_dir / "fastapi_todo_test.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{_db_path}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """Yield a new SQLAlchemy session and ensure it is closed after use."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def _create_tables():
    # Import models to register them with Base
    from . import models
    Base.metadata.create_all(bind=engine)

# Create tables at import time.
_create_tables()
