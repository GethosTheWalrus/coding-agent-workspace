"""Application configuration."""

import os
from typing import Optional


class Settings:
    """Application settings loaded from environment variables."""

    # Application
    app_name: str = os.getenv("APP_NAME", "Todo API")
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"

    # Database
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./data/todo.db")

    # Test database (used during testing)
    test_database_url: Optional[str] = os.getenv("TEST_DATABASE_URL")


settings = Settings()
