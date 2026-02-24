"""Database session handling utilities.

TODO: Implement a function `get_db` that yields a SQLAlchemy session
and ensures proper cleanup. Use the `SQLITE_DB_PATH` environment variable
or default to `/data/app.db`.
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

SQLITE_DB_PATH = os.getenv("SQLITE_DB_PATH", "/data/app.db")
SQLALCHEMY_DATABASE_URL = f"sqlite:///{SQLITE_DB_PATH}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    """Yield a database session and close it after use.

    TODO: Implement proper context management.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
