"""API router for Todo endpoints.

All route handlers should use the CRUD functions defined in `app.crud`
and the database dependency from `app.database`.

TODO: Implement the following endpoints:
- POST /todos/
- GET /todos/
- GET /todos/{id}
- PUT /todos/{id}
- DELETE /todos/{id}
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schemas, database

router = APIRouter(prefix="/todos", tags=["todos"])

# TODO: Implement route handlers using crud functions and DB dependency
