"""Pydantic schemas for the Todo API.

These schemas define the shape of data that the API accepts (input) and
returns (output). ``BaseModel`` from Pydantic v2 is used.
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field, ConfigDict


class TodoBase(BaseModel):
    """Fields shared between create and update operations."""

    title: str = Field(..., max_length=255, description="Short title of the todo item")
    description: Optional[str] = Field(None, description="Longer description of the todo")
    completed: bool = Field(False, description="Completion status")

    # Enable ORM mode for compatibility with SQLAlchemy models
    model_config = ConfigDict(from_attributes=True)


class TodoCreate(TodoBase):
    """Schema used when creating a new todo item."""

    pass


class TodoUpdate(BaseModel):
    """Schema for partial updates – all fields are optional."""

    title: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None
    completed: Optional[bool] = None

    model_config = ConfigDict(from_attributes=True)


class TodoInDBBase(TodoBase):
    """Base schema that includes DB‑generated fields."""

    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class Todo(TodoInDBBase):
    """Schema returned to clients – mirrors the DB model."""

    pass


class TodoList(BaseModel):
    """Wrapper for a list of todos – useful for pagination later."""

    todos: List[Todo]
    total: int

    model_config = ConfigDict(from_attributes=True)
