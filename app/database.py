"""Database configuration and session management.

This module creates the SQLite engine, the session maker, and provides a
FastAPI dependency (`get_session`) that yields a database session for each
request.  The session is automatically closed after the request finishes.
"""

from pathlib import Path
from typing import Generator

from sqlmodel import Session, SQLModel, create_engine

# Database URL – using a file named `sqlite.db` in the project root.
# In production you might load this from an environment variable.
DATABASE_URL = "sqlite:///./sqlite.db"

# `connect_args` with `check_same_thread=False` is required for SQLite when
# using multiple threads (as Uvicorn does).
engine = create_engine(
    DATABASE_URL, echo=False, connect_args={"check_same_thread": False}
)


def create_db_and_tables() -> None:
    """Create database tables based on the SQLModel models.

    This should be called once at application startup.
    """
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """FastAPI dependency that provides a database session.

    Yields
    ------
    Session
        SQLModel session bound to the engine.
    """
    with Session(engine) as session:
        yield session
