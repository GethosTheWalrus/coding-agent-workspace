# app/schemas.py
"""Pydantic schemas for request validation and response models.

These schemas define the shape of data exchanged via the API.
"""

from pydantic import BaseModel
from typing import Optional

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoCreate(TodoBase):
    """Schema for creating a new Todo. Inherits all fields from TodoBase.
    """
    pass

class TodoUpdate(BaseModel):
    """Schema for updating a Todo. All fields are optional to allow partial updates.
    """
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class TodoRead(TodoBase):
    id: int

    class Config:
        orm_mode = True
