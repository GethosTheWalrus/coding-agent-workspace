"""Application configuration."""
import os
from typing import Any
from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    model_config = ConfigDict(env_file=".env", case_sensitive=True)
    
    # Database configuration
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///todos.db")
    
    # Application settings
    app_name: str = "Todo API"
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"


# Global settings instance
settings = Settings()