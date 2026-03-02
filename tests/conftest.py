"""Pytest fixtures for testing."""
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.database import Base, get_db
from app.main import app
from app.models import Todo


# Use in-memory SQLite for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db_session():
    """
    Create a fresh database session for each test.
    
    Yields:
        Session: SQLAlchemy database session
    """
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    # Create a new session
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
    
    # Drop all tables after test
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    """
    Create a test client with a mock database session.
    
    Args:
        db_session: Database session fixture
    
    Yields:
        TestClient: FastAPI test client
    """
    def override_get_db():
        try:
            yield db_session
        finally:
            pass
    
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture(scope="function")
def sample_todo_data():
    """Sample todo data for testing."""
    return {
        "title": "Test Todo",
        "description": "This is a test todo item"
    }


@pytest.fixture(scope="function")
def created_todo(db_session, sample_todo_data):
    """Create a todo in the database for testing."""
    todo = Todo(
        title=sample_todo_data["title"],
        description=sample_todo_data["description"],
        completed=False
    )
    db_session.add(todo)
    db_session.commit()
    db_session.refresh(todo)
    return todo