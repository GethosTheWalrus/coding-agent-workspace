"""Pytest fixtures and configuration for testing."""

import os
import tempfile
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from fastapi.testclient import TestClient

# Create a temporary file for the test database
TEST_DB_PATH = tempfile.mktemp(suffix=".db")
os.environ["DATABASE_URL"] = f"sqlite:///{TEST_DB_PATH}"

from app.main import app
from app.database import Base, get_db


@pytest.fixture(scope="function")
def test_engine():
    """
    Create a fresh test database engine for each test function.

    Uses a file-based SQLite database for proper isolation.
    """
    # Create a unique database file for each test
    db_path = tempfile.mktemp(suffix=".db")

    # Use file-based database for tests
    engine = create_engine(
        f"sqlite:///{db_path}", connect_args={"check_same_thread": False}
    )

    # Create all tables using the Base from app.database
    Base.metadata.create_all(bind=engine)

    yield engine

    # Cleanup
    Base.metadata.drop_all(bind=engine)
    # Remove the database file
    try:
        os.remove(db_path)
    except OSError:
        pass


@pytest.fixture(scope="function")
def test_db(test_engine):
    """
    Create a database session for each test function.

    Provides direct database access for CRUD tests.
    """
    TestingSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=test_engine
    )

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def client(test_engine):
    """
    Create a test client for making HTTP requests.

    The client uses a file-based test database.
    """
    # Create session factory for the test engine
    TestingSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=test_engine
    )

    # Override the get_db dependency
    def override_get_db() -> Session:
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    # Remove the dependency override
    app.dependency_overrides.clear()


@pytest.fixture(scope="function")
def sample_todo_data():
    """Sample todo data for testing."""
    return {
        "title": "Test Todo",
        "description": "This is a test todo item",
        "completed": False,
    }
