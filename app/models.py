"""SQLModel definitions for the Todo application.

The `Todo` model represents a todo item stored in the SQLite database.
It inherits from `SQLModel` which provides both ORM capabilities (via
SQLAlchemy) and Pydantic validation/serialization.
"""

from typing import Optional
from datetime import datetime

from sqlmodel import Field, SQLModel


class TodoBase(SQLModel):
    """Base attributes shared between create and read models."""
    title: str = Field(index=True, description="Title of the todo item")
    description: Optional[str] = Field(default=None, description="Detailed description")
    completed: bool = Field(default=False, description="Completion status")
    due_date: Optional[datetime] = Field(default=None, description="Optional due date")


class Todo(TodoBase, table=True):
    """Full model stored in the database, includes primary key."""
    id: Optional[int] = Field(default=None, primary_key=True)


class TodoCreate(TodoBase):
    """Model used when creating a new todo (no id)."""
    pass


class TodoRead(TodoBase):
    """Model returned to clients (includes id)."""
    id: int


class TodoUpdate(SQLModel):
    """Model for partial updates – all fields optional."""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    due_date: Optional[datetime] = None
