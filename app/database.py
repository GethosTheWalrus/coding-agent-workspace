"""Database session handling utilities.

Provides a FastAPI dependency `get_db` that yields a SQLAlchemy session
and ensures it is closed after the request.
"""

import os
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# Default to a temporary file path if SQLITE_DB_PATH not set; ensures write permission.
SQLITE_DB_PATH = os.getenv("SQLITE_DB_PATH", "/tmp/app.db")
SQLALCHEMY_DATABASE_URL = f"sqlite:///{SQLITE_DB_PATH}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator[Session, None, None]:
    """FastAPI dependency that provides a database session.

    Yields:
        Session: SQLAlchemy session object.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
