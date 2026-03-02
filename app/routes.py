"""API routes for Todo operations."""

from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .database import get_db
from .schemas import TodoCreate, TodoUpdate, TodoResponse, TodoListResponse
from .crud import (
    create_todo,
    get_todo,
    get_todos,
    update_todo,
    delete_todo,
    get_todo_count,
)

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post(
    "",
    response_model=TodoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new todo",
    description="Create a new todo item with the provided data",
)
def create(todo: TodoCreate, db: Session = Depends(get_db)) -> TodoResponse:
    """
    Create a new todo item.

    - **title**: Required, the title of the todo (1-255 characters)
    - **description**: Optional, detailed description
    - **completed**: Optional, defaults to False
    """
    db_todo = create_todo(db, todo)
    return TodoResponse.model_validate(db_todo)


@router.get(
    "",
    response_model=TodoListResponse,
    summary="List all todos",
    description="Retrieve all todo items with optional filtering and pagination",
)
def list_todos(
    skip: int = 0,
    limit: int = 100,
    completed: Optional[bool] = None,
    db: Session = Depends(get_db),
) -> TodoListResponse:
    """
    Retrieve all todo items.

    - **skip**: Number of items to skip for pagination
    - **limit**: Maximum number of items to return
    - **completed**: Filter by completion status (optional)
    """
    items = get_todos(db, skip=skip, limit=limit, completed=completed)
    total = get_todo_count(db, completed=completed)

    return TodoListResponse(
        items=[TodoResponse.model_validate(item) for item in items],
        total=total,
        page=skip // limit + 1 if limit > 0 else 1,
        page_size=limit,
    )


@router.get(
    "/{todo_id}",
    response_model=TodoResponse,
    summary="Get a todo by ID",
    description="Retrieve a specific todo item by its ID",
)
def read(todo_id: int, db: Session = Depends(get_db)) -> TodoResponse:
    """
    Retrieve a specific todo item.

    - **todo_id**: The ID of the todo to retrieve
    """
    db_todo = get_todo(db, todo_id=todo_id)

    if db_todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id {todo_id} not found",
        )

    return TodoResponse.model_validate(db_todo)


@router.put(
    "/{todo_id}",
    response_model=TodoResponse,
    summary="Update a todo",
    description="Update an existing todo item",
)
def update(
    todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)
) -> TodoResponse:
    """
    Update a todo item.

    - **todo_id**: The ID of the todo to update
    - All fields are optional; only provided fields will be updated
    """
    db_todo = update_todo(db, todo_id=todo_id, todo_update=todo)

    if db_todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id {todo_id} not found",
        )

    return TodoResponse.model_validate(db_todo)


@router.delete(
    "/{todo_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a todo",
    description="Delete a todo item",
)
def delete(todo_id: int, db: Session = Depends(get_db)) -> None:
    """
    Delete a todo item.

    - **todo_id**: The ID of the todo to delete
    """
    success = delete_todo(db, todo_id=todo_id)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id {todo_id} not found",
        )
