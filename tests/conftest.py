"""Pytest fixtures and configuration for testing."""
import os
import tempfile
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import app modules
import sys
sys.path.insert(0, 'src')

from app.main import app
from app.database import Base, get_db
from app.models import Todo


@pytest.fixture(scope="function")
def db_session():
    """Create a fresh database session for each test with a temporary file.
    
    Yields:
        Database session with clean state
    """
    # Create a temporary database file for this test
    temp_db_file = tempfile.mktemp(suffix=".db")
    db_url = f"sqlite:///{temp_db_file}"
    
    # Create engine and tables
    test_engine = create_engine(
        db_url,
        connect_args={"check_same_thread": False}
    )
    Base.metadata.create_all(bind=test_engine)
    
    # Create session
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
    db = TestingSessionLocal()
    
    try:
        yield db
    finally:
        db.close()
        # Cleanup temp file
        if os.path.exists(temp_db_file):
            os.remove(temp_db_file)


@pytest.fixture(scope="function")
def client(db_session):
    """Create a test client with a mock database session.
    
    Args:
        db_session: Database session fixture (tables already created)
        
    Yields:
        TestClient instance
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
        "description": "This is a test todo item",
        "completed": False
    }


@pytest.fixture(scope="function")
def created_todo(db_session, sample_todo_data):
    """Create a todo in the database for testing."""
    from app.crud import create_todo
    from app.schemas import TodoCreate
    
    todo = TodoCreate(**sample_todo_data)
    return create_todo(db=db_session, todo=todo)