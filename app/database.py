"""Database utilities for the Todo API.

This module creates a SQLite engine using SQLModel and provides a helper
function to initialise the database schema.
"""

from pathlib import Path
from sqlmodel import SQLModel, create_engine, Session

# SQLite file in the project root
DATABASE_URL = "sqlite:///./todo.db"

engine = create_engine(
    DATABASE_URL,
    echo=False,
    connect_args={"check_same_thread": False},
)

def init_db() -> None:
    """Create database tables if they do not exist.

    This function is idempotent – calling it multiple times will not raise
    errors because SQLModel's ``create_all`` only creates missing tables.
    """
    SQLModel.metadata.create_all(engine)

def get_session() -> Session:
    """Return a new SQLModel session bound to the engine.

    The caller is responsible for closing the session (e.g. using a context
    manager ``with get_session() as session:``).
    """
    # Ensure tables exist before creating a session. This handles cases where
    # the database file has been removed (e.g., by test fixtures) after the
    # module was imported.
    init_db()
    return Session(engine)
