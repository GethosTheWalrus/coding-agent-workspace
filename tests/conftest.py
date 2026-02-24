# tests/conftest.py
"""Pytest fixtures for the FastAPI Todo API tests.

Provides a TestClient instance with a temporary SQLite database for
isolated testing.
"""

import os
import tempfile
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app import models
from app.database import Base, get_db

# Create a temporary SQLite file for each test session
@pytest.fixture(scope="session")
def db_url():
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    yield f"sqlite:///{path}"
    os.remove(path)

@pytest.fixture(scope="session")
def engine(db_url):
    return create_engine(db_url, connect_args={"check_same_thread": False})

@pytest.fixture(scope="session")
def tables(engine):
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db_session(engine, tables):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

# Override the FastAPI dependency to use the test DB session
@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
