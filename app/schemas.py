"""Pydantic schemas for request and response models.

These schemas define the shape of data exchanged via the API. Updated for
Pydantic v2 where ``Config`` is deprecated – we use ``model_config`` with
``ConfigDict`` to enable ORM mode.
"""

from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class TodoBase(BaseModel):
    title: str = Field(..., example="Buy groceries")
    description: Optional[str] = Field(None, example="Milk, eggs, bread")
    completed: bool = Field(False, example=False)

    model_config = ConfigDict(from_attributes=True)

class TodoCreate(TodoBase):
    """Schema for creating a new todo item. Inherits all fields from ``TodoBase``.
    """

    pass

class TodoUpdate(BaseModel):
    """Schema for updating an existing todo item. All fields are optional to allow
    partial updates.
    """

    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

    model_config = ConfigDict(from_attributes=True)

class TodoRead(TodoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
