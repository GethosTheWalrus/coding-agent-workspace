"""Database configuration and session management for the Todo API.

- Uses SQLite as the database engine.
- Provides a SQLAlchemy `engine` and a `SessionLocal` factory.
- Includes a dependency `get_db` for FastAPI routes to obtain a session.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pathlib import Path

# SQLite database file (placed in the project root)
SQLITE_DB_PATH = Path(__file__).resolve().parent.parent / "todo.db"

# SQLAlchemy engine – echo=False for production, True for debugging
engine = create_engine(f"sqlite:///{SQLITE_DB_PATH}", connect_args={"check_same_thread": False})

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency for FastAPI routes
def get_db():
    """Yield a new SQLAlchemy session and ensure it is closed after use."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
