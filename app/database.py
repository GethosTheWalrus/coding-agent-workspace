"""Database configuration for the FastAPI Todo API.

This module sets up the SQLAlchemy engine, session factory, and a base class for
model declarations.  The backend developer will ensure proper handling of the
SQLite database file and session lifecycle.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite URL – the file will be created in the working directory.
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# Connect arguments for SQLite – ``check_same_thread=False`` allows usage in
# async contexts (FastAPI's default thread pool).
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal class – each request will get a new session instance.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for model definitions.
Base = declarative_base()

# Dependency to be used in FastAPI routes (to be imported where needed).
def get_db():
    """Yield a new SQLAlchemy session and ensure it is closed after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
