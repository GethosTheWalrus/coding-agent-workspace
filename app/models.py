"""SQLModel definitions for Todo items.

The Todo model represents the database table. The TodoCreate, TodoRead,
and TodoUpdate schemas are used for request validation and response
serialization, respectively.
"""

from typing import Optional
from sqlmodel import Field, SQLModel

class TodoBase(SQLModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class Todo(TodoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class TodoCreate(TodoBase):
    """Schema for creating a new Todo item."""
    pass

class TodoRead(TodoBase):
    """Schema for reading Todo items from the API."""
    id: int

class TodoUpdate(SQLModel):
    """Schema for updating an existing Todo item. All fields are optional."""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
