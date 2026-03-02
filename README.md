# Todo API

A REST API for a todo application built with FastAPI and SQLite.

## Features

- Create, read, update, and delete todo items
- Automatic OpenAPI documentation at `/docs`
- SQLite database for simple file-based storage
- Automated tests with 90%+ code coverage
- CI/CD pipeline with GitHub Actions

## Requirements

- Python 3.10+
- pip

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd todo-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the development server:
```bash
uvicorn src.app.main:app --reload
```

The API will be available at `http://localhost:8000`.

## API Endpoints

### Root
- `GET /` - Get API information

### Todos
- `POST /todos/` - Create a new todo
- `GET /todos/` - List all todos
- `GET /todos/{todo_id}` - Get a specific todo
- `PUT /todos/{todo_id}` - Update a todo
- `DELETE /todos/{todo_id}` - Delete a todo

## API Examples

### Create a Todo
```bash
curl -X POST "http://localhost:8000/todos/" \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk, eggs, bread", "completed": false}'
```

### List All Todos
```bash
curl "http://localhost:8000/todos/"
```

### Get a Todo
```bash
curl "http://localhost:8000/todos/1"
```

### Update a Todo
```bash
curl -X PUT "http://localhost:8000/todos/1" \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "completed": true}'
```

### Delete a Todo
```bash
curl -X DELETE "http://localhost:8000/todos/1"
```

## Running Tests

Run all tests with coverage:
```bash
pytest --cov=src/app --cov-report=term-missing -v
```

Run tests with coverage report in HTML:
```bash
pytest --cov=src/app --cov-report=html -v
```

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── ci.yml          # CI/CD pipeline
├── src/
│   └── app/
│       ├── __init__.py
│       ├── main.py         # FastAPI application
│       ├── config.py       # Configuration
│       ├── database.py     # Database setup
│       ├── models.py       # SQLAlchemy models
│       ├── schemas.py      # Pydantic schemas
│       ├── crud.py         # CRUD operations
│       └── routes.py       # API routes
├── tests/
│   ├── __init__.py
│   ├── conftest.py         # Test fixtures
│   ├── test_crud.py        # CRUD tests
│   └── test_api.py         # API tests
├── requirements.txt        # Dependencies
└── README.md              # This file
```

## Configuration

Environment variables:
- `DATABASE_URL` - Database connection string (default: `sqlite:///todos.db`)
- `DEBUG` - Enable debug mode (default: `false`)

## License

MIT