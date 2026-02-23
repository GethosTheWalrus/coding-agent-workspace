"""Database configuration for the FastAPI Todo app.

We use SQLite with SQLAlchemy's ORM. The `engine` is created once and
`SessionLocal` provides a new session per request. The `Base` class is used
for model declarations.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLITE_DB_URL = "sqlite:///./todo.db"

# Connect arguments for SQLite to allow usage in multithreaded environments
engine = create_engine(
    SQLITE_DB_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """Yield a new database session.

    FastAPI's dependency injection system will call this function for each
    request that includes `Depends(get_db)`. The session is closed after the
    request is processed.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
