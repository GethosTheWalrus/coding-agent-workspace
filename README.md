# Todo API

A simple Todo REST API built with FastAPI and SQLite.

## Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the development server
uvicorn app.main:app --reload
```

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/todos/` | Create a new todo |
| `GET`  | `/todos/` | List all todos |
| `GET`  | `/todos/{todo_id}` | Retrieve a specific todo |
| `PUT`  | `/todos/{todo_id}` | Update a todo |
| `DELETE` | `/todos/{todo_id}` | Delete a todo |
