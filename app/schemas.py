"""Pydantic schemas for the Todo API.

These schemas define the shape of data that the API accepts (input) and
returns (output). ``BaseModel`` from Pydantic v2 is used.
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TodoBase(BaseModel):
    """Fields shared between create and update operations."""

    title: str = Field(..., max_length=255, description="Short title of the todo item")
    description: Optional[str] = Field(None, description="Longer description of the todo")
    completed: bool = Field(False, description="Completion status")

    class Config:
        orm_mode = True


class TodoCreate(TodoBase):
    """Schema used when creating a new todo item."""

    pass


class TodoUpdate(BaseModel):
    """Schema for partial updates – all fields are optional."""

    title: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None
    completed: Optional[bool] = None

    class Config:
        orm_mode = True


class TodoInDBBase(TodoBase):
    """Base schema that includes DB‑generated fields."""

    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Todo(TodoInDBBase):
    """Schema returned to clients – mirrors the DB model."""

    pass


class TodoList(BaseModel):
    """Wrapper for a list of todos – useful for pagination later."""

    todos: list[Todo]
    total: int

    class Config:
        orm_mode = True
