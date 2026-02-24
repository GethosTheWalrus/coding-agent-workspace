"""Database utilities for the Todo API.

Provides a SQLModel engine bound to a SQLite file and a session
dependency that can be injected into FastAPI routes.
"""

from sqlmodel import SQLModel, create_engine, Session
from pathlib import Path

# SQLite file location (relative to project root)
DATABASE_URL = "sqlite:///./todo.db"

# Engine with connect_args for SQLite foreign keys support
engine = create_engine(
    DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
)


def create_db_and_tables() -> None:
    """Create database tables based on SQLModel models.
    """
    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    """FastAPI dependency that provides a database session.
    
    Usage::
        def read_items(session: Session = Depends(get_session)):
            ...
    """
    with Session(engine) as session:
        yield session
