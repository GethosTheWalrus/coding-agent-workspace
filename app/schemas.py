"""Pydantic schemas for request/response validation."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class TodoCreate(BaseModel):
    """Schema for creating a new todo item."""
    
    title: str = Field(..., min_length=1, max_length=255, description="Todo title")
    description: Optional[str] = Field(None, max_length=1000, description="Todo description")


class TodoUpdate(BaseModel):
    """Schema for updating an existing todo item."""
    
    title: Optional[str] = Field(None, min_length=1, max_length=255, description="Todo title")
    description: Optional[str] = Field(None, max_length=1000, description="Todo description")
    completed: Optional[bool] = Field(None, description="Completion status")


class TodoResponse(BaseModel):
    """Schema for todo response data."""
    
    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        """Pydantic configuration for ORM mode."""
        from_attributes = True


class MessageResponse(BaseModel):
    """Schema for simple message responses."""
    
    message: str