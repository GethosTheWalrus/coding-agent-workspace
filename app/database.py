from sqlmodel import SQLModel, create_engine, Session
from pathlib import Path

SQLITE_DB_PATH = Path(__file__).parent.parent / "todo.db"
engine = create_engine(f"sqlite:///{SQLITE_DB_PATH}", echo=False)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    return Session(engine)
