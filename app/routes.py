"""API route definitions for the Todo API."""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Todo
from app.schemas import TodoCreate, TodoUpdate, TodoResponse, MessageResponse
from app.crud import create_todo, get_todo, get_all_todos, update_todo, delete_todo

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo_endpoint(todo: TodoCreate, db: Session = Depends(get_db)) -> Todo:
    """
    Create a new todo item.
    
    Args:
        todo: TodoCreate schema with title and optional description
        db: Database session
    
    Returns:
        Created todo item
    """
    return create_todo(db=db, todo=todo)


@router.get("/", response_model=List[TodoResponse])
def list_todos_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> List[Todo]:
    """
    Get all todo items.
    
    Args:
        skip: Number of items to skip (for pagination)
        limit: Maximum number of items to return
        db: Database session
    
    Returns:
        List of todo items
    """
    return get_all_todos(db=db, skip=skip, limit=limit)


@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo_endpoint(todo_id: int, db: Session = Depends(get_db)) -> Todo:
    """
    Get a specific todo item by ID.
    
    Args:
        todo_id: The ID of the todo to retrieve
        db: Database session
    
    Returns:
        The todo item
    
    Raises:
        HTTPException: 404 if todo not found
    """
    todo = get_todo(db=db, todo_id=todo_id)
    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id {todo_id} not found"
        )
    return todo


@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo_endpoint(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)) -> Todo:
    """
    Update an existing todo item.
    
    Args:
        todo_id: The ID of the todo to update
        todo: TodoUpdate schema with fields to update
        db: Database session
    
    Returns:
        Updated todo item
    
    Raises:
        HTTPException: 404 if todo not found
    """
    updated_todo = update_todo(db=db, todo_id=todo_id, todo=todo)
    if updated_todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id {todo_id} not found"
        )
    return updated_todo


@router.delete("/{todo_id}", response_model=MessageResponse)
def delete_todo_endpoint(todo_id: int, db: Session = Depends(get_db)) -> MessageResponse:
    """
    Delete a todo item.
    
    Args:
        todo_id: The ID of the todo to delete
        db: Database session
    
    Returns:
        Success message
    
    Raises:
        HTTPException: 404 if todo not found
    """
    deleted = delete_todo(db=db, todo_id=todo_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id {todo_id} not found"
        )
    return MessageResponse(message="Todo deleted successfully")