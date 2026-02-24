# app/database.py
"""Database configuration and helper utilities.

The SQLite database lives in a file named ``todo.db`` at the project root.
SQLModel's ``create_engine`` is used to obtain an engine, and a ``Session``
factory is provided for request‑scoped interactions.
"""

from pathlib import Path
from sqlmodel import Session, SQLModel, create_engine

# Path to the SQLite file – placed in the project root for simplicity.
DATABASE_URL = f"sqlite:///{Path(__file__).resolve().parent.parent / 'todo.db'}"

# ``connect_args`` with ``check_same_thread=False`` is required for SQLite when
# using multiple threads (e.g., the FastAPI test client).
engine = create_engine(DATABASE_URL, echo=False, connect_args={"check_same_thread": False})

def create_db_and_tables() -> None:
    """Create database tables based on the SQLModel models.

    This function is idempotent – calling it multiple times will not raise an
    error because SQLModel/SQLAlchemy will only create tables that do not yet
    exist.
    """
    SQLModel.metadata.create_all(engine)

def get_session() -> Session:
    """Yield a new SQLModel ``Session``.

    The function is intended for use with FastAPI's ``Depends`` system.
    """
    with Session(engine) as session:
        yield session
