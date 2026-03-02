"""Pydantic schemas for request/response validation."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class TodoBase(BaseModel):
    """Base schema for todo items."""

    title: str = Field(
        ..., min_length=1, max_length=255, description="The title of the todo item"
    )
    description: Optional[str] = Field(
        None, max_length=1000, description="Optional description"
    )
    completed: bool = Field(False, description="Completion status")


class TodoCreate(TodoBase):
    """Schema for creating a new todo item."""

    pass


class TodoUpdate(BaseModel):
    """Schema for updating an existing todo item. All fields are optional."""

    title: Optional[str] = Field(
        None, min_length=1, max_length=255, description="The title of the todo item"
    )
    description: Optional[str] = Field(
        None, max_length=1000, description="Optional description"
    )
    completed: Optional[bool] = Field(None, description="Completion status")


class TodoResponse(TodoBase):
    """Schema for todo item responses (includes id and timestamps)."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None


class TodoListResponse(BaseModel):
    """Schema for listing todos with pagination."""

    items: list[TodoResponse]
    total: int
    page: int = 1
    page_size: int = 100
