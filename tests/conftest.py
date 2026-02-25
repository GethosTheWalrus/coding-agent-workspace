"""Pytest fixtures for the FastAPI application.

Provides a TestClient with a file‑based SQLite database for isolated tests.
"""

import sys
import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Ensure the app package is importable when tests are run from the repository root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app
from app import database, models

# Use a file‑based SQLite DB to keep the schema across connections
TEST_DB_PATH = "./test.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{TEST_DB_PATH}"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Dependency override
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[database.get_db] = override_get_db

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

# Cleanup after tests
def teardown_module(module):
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)
