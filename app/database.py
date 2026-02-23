from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager

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

@contextmanager
def get_db():
    """Yield a database session and ensure it is closed after use."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
