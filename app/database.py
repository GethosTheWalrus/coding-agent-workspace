# app/database.py
"""Database configuration and session management.

- Creates a SQLite engine.
- Provides a `SessionLocal` factory for dependency injection.
- Declares a `Base` class for model definitions.
- Supplies a FastAPI dependency `get_db` that yields a session.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Generator

SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"
# For SQLite we need to set `check_same_thread` to False when using
# multiple threads (e.g., in async contexts).
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db() -> Generator:
    """FastAPI dependency that provides a database session.

    Yields a SQLAlchemy Session and ensures it is closed after the request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
