"""Pydantic schemas for request and response models.

These schemas define the shape of data exchanged via the API.  The backend
developer will implement any additional validation logic (e.g., length checks).
"""

from pydantic import BaseModel, Field
from typing import Optional


class TodoBase(BaseModel):
    title: str = Field(..., example="Buy groceries")
    description: Optional[str] = Field(None, example="Milk, eggs, bread")
    completed: bool = Field(False, example=False)


class TodoCreate(TodoBase):
    """Schema for creating a new todo item.  Inherits all fields from ``TodoBase``.
    """

    pass


class TodoUpdate(BaseModel):
    """Schema for updating an existing todo item.  All fields are optional to allow
    partial updates.
    """

    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TodoRead(TodoBase):
    id: int

    class Config:
        orm_mode = True
