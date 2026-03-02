# Todo API

A RESTful API for managing todo items, built with FastAPI and SQLite.

## Features

- Create, read, update, and delete todo items
- Automatic OpenAPI documentation at `/docs`
- Pagination support for listing todos
- Filter todos by completion status
- 90%+ test coverage
- Docker support
- CI/CD pipeline with GitHub Actions

## Quick Start

### Prerequisites

- Python 3.11 or higher
- Docker (optional)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd todo-api
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

### Using Docker

Build and run the Docker container:
```bash
docker build -t todo-api .
docker run -p 8000:8000 todo-api
```

## API Endpoints

### Todos

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/todos` | Create a new todo |
| GET | `/todos` | List all todos |
| GET | `/todos/{id}` | Get a specific todo |
| PUT | `/todos/{id}` | Update a todo |
| DELETE | `/todos/{id}` | Delete a todo |

### Other

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information |
| GET | `/health` | Health check |
| GET | `/docs` | OpenAPI documentation |
| GET | `/redoc` | ReDoc documentation |

## API Usage Examples

### Create a Todo

```bash
curl -X POST "http://localhost:8000/todos" \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk, eggs, bread"}'
```

Response:
```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": false,
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": null
}
```

### List Todos

```bash
curl "http://localhost:8000/todos"
```

Response:
```json
{
  "items": [
    {
      "id": 1,
      "title": "Buy groceries",
      "description": "Milk, eggs, bread",
      "completed": false,
      "created_at": "2024-01-01T00:00:00Z",
      "updated_at": null
    }
  ],
  "total": 1,
  "page": 1,
  "page_size": 100
}
```

### Update a Todo

```bash
curl -X PUT "http://localhost:8000/todos/1" \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'
```

### Delete a Todo

```bash
curl -X DELETE "http://localhost:8000/todos/1"
```

## Testing

Run all tests:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=app --cov-report=term-missing
```

Run tests with HTML coverage report:
```bash
pytest --cov=app --cov-report=html
```

## Configuration

Environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `DATABASE_URL` | `sqlite:///./todo.db` | Database connection string |
| `APP_NAME` | `Todo API` | Application name |
| `DEBUG` | `false` | Enable debug mode |

## Project Structure

```
todo-api/
├── app/
│   ├── main.py          # FastAPI application
│   ├── config.py        # Configuration
│   ├── database.py      # Database setup
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py          # CRUD operations
│   └── routes.py        # API routes
├── tests/
│   ├── conftest.py      # Test fixtures
│   ├── test_crud.py     # CRUD tests
│   └── test_api.py      # API tests
├── .github/
│   └── workflows/
│       └── ci.yml       # CI/CD pipeline
├── Dockerfile
├── requirements.txt
├── pytest.ini
└── README.md
```

## License

MIT