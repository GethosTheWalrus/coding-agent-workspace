"""API routes for Todo CRUD operations."""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .database import get_db
from .models import Todo
from .schemas import TodoCreate, TodoUpdate, TodoResponse
from . import crud

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)) -> Todo:
    """Create a new todo item.
    
    Args:
        todo: TodoCreate schema with todo data
        db: Database session
        
    Returns:
        Created todo item
    """
    return crud.create_todo(db=db, todo=todo)


@router.get("/", response_model=List[TodoResponse])
def read_todos(
    skip: int = 0,
    limit: int = 100,
    completed: bool = None,
    db: Session = Depends(get_db)
) -> List[Todo]:
    """Retrieve all todo items with optional filtering.
    
    Args:
        skip: Number of items to skip (for pagination)
        limit: Maximum number of items to return
        completed: Optional filter by completion status
        db: Database session
        
    Returns:
        List of todo items
    """
    return crud.get_todos(db=db, skip=skip, limit=limit, completed=completed)


@router.get("/{todo_id}", response_model=TodoResponse)
def read_todo(todo_id: int, db: Session = Depends(get_db)) -> Todo:
    """Retrieve a single todo item by ID.
    
    Args:
        todo_id: ID of the todo to retrieve
        db: Database session
        
    Returns:
        Todo item
        
    Raises:
        HTTPException: 404 if todo not found
    """
    todo = crud.get_todo(db=db, todo_id=todo_id)
    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id {todo_id} not found"
        )
    return todo


@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo_update: TodoUpdate, db: Session = Depends(get_db)) -> Todo:
    """Update an existing todo item.
    
    Args:
        todo_id: ID of the todo to update
        todo_update: TodoUpdate schema with updated data
        db: Database session
        
    Returns:
        Updated todo item
        
    Raises:
        HTTPException: 404 if todo not found
    """
    todo = crud.update_todo(db=db, todo_id=todo_id, todo_update=todo_update)
    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id {todo_id} not found"
        )
    return todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)) -> None:
    """Delete a todo item by ID.
    
    Args:
        todo_id: ID of the todo to delete
        db: Database session
        
    Raises:
        HTTPException: 404 if todo not found
    """
    if not crud.delete_todo(db=db, todo_id=todo_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id {todo_id} not found"
        )