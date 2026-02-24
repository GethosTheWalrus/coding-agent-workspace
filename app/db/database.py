"""Database configuration for the Todo API.

Provides the SQLAlchemy engine, a session factory, and a dependency
function that yields a session per request.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./todo.db"
# SQLite needs `check_same_thread=False` when used with SQLAlchemy's
# connection pool in a multithreaded environment (e.g., Uvicorn workers).
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal will be used in FastAPI dependencies to provide a DB session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models.
Base = declarative_base()

# Dependency that can be used with FastAPI's Depends to get a DB session.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
