"""Database configuration for the Todo API.

This module sets up the SQLAlchemy engine, session factory, and a helper
function to obtain a session that can be used with FastAPI's dependency
injection system.
"""

from __future__ import annotations

from pathlib import Path
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# SQLite database file – placed in the project root for simplicity.
BASE_DIR = Path(__file__).resolve().parent.parent
SQLITE_DB_PATH = BASE_DIR / "todo.db"

# SQLAlchemy engine – echo=False for production, can be toggled via env.
engine = create_engine(
    f"sqlite+pysqlite:///{SQLITE_DB_PATH}",
    echo=False,
    future=True,
)

# Session factory – ``autocommit=False`` and ``autoflush=False`` are the
# recommended defaults for most applications.
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)

# Base class for declarative models.
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    """FastAPI dependency that provides a database session.

    The session is yielded to the path operation function and closed
    automatically after the request is finished.
    """
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
