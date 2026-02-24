# app/routers/todo.py
"""Todo router defining API endpoints.

TODO: Implement the following endpoints using FastAPI:
- `POST /todos/` – create a new todo.
- `GET /todos/` – list all todos.
- `GET /todos/{todo_id}` – retrieve a specific todo.
- `PUT /todos/{todo_id}` – update a todo.
- `DELETE /todos/{todo_id}` – delete a todo.

Each endpoint should use the appropriate Pydantic schemas from
`app.schemas` and call the corresponding functions in `app.crud`.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/todos", tags=["todos"])

# TODO: Define endpoint functions here
