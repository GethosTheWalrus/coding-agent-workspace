import os
import sys
import pathlib
import pytest

# Ensure the project root is in sys.path for imports
ROOT_DIR = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# Ensure a fresh SQLite database for each test session
@pytest.fixture(scope="session", autouse=True)
def setup_database():
    db_path = ROOT_DIR / "test.db"
    if db_path.exists():
        db_path.unlink()
    # Import the app to trigger table creation via database._create_tables()
    from app import database  # noqa: F401
    # Ensure tables are created (in case import didn't)
    database._create_tables()
    yield
    # Cleanup after tests
    if db_path.exists():
        db_path.unlink()
