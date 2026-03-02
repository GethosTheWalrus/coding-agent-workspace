"""Pydantic schemas for request/response validation."""
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class TodoBase(BaseModel):
    """Base schema for todo items."""
    title: str = Field(..., min_length=1, max_length=255, description="The title of the todo item")
    description: Optional[str] = Field(None, max_length=1000, description="Description of the todo item")
    completed: bool = Field(default=False, description="Whether the todo is completed")


class TodoCreate(TodoBase):
    """Schema for creating a new todo item."""
    pass


class TodoUpdate(BaseModel):
    """Schema for updating a todo item. All fields are optional."""
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    completed: Optional[bool] = None


class TodoResponse(TodoBase):
    """Schema for todo item response (includes ID)."""
    id: int
    
    model_config = ConfigDict(from_attributes=True)