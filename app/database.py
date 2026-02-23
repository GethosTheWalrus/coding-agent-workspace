from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite URL – using a file named 'todos.db' in the project root
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# Connect arguments for SQLite to allow usage in multithreaded environments
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal class for creating DB sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()

def init_db():
    """Create all tables in the database (if they don't exist)."""
    Base.metadata.create_all(bind=engine)

# FastAPI dependency that provides a DB session and ensures it is closed after use.
def get_db():
    """Yield a database session for FastAPI dependencies.

    This function is a generator (uses ``yield``) so FastAPI can treat it as a
    dependency that provides a resource and performs cleanup after the request
    is processed.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
