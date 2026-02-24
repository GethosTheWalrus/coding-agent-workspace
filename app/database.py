from sqlmodel import SQLModel, create_engine, Session
from pathlib import Path
from contextlib import contextmanager

SQLITE_DB_PATH = Path(__file__).parent.parent / "todo.db"
engine = create_engine(f"sqlite:///{SQLITE_DB_PATH}", echo=False)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@contextmanager
def get_session():
    with Session(engine) as session:
        yield session
