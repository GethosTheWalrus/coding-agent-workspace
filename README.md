# Todo API

A REST API for managing todo items built with FastAPI and SQLite.

## Features

- Create, read, update, and delete todo items
- RESTful API design
- Automatic OpenAPI documentation
- SQLite database for persistence
- Comprehensive test suite with 90%+ coverage
- CI/CD pipeline with GitHub Actions
- Docker support for containerized deployment

## Requirements

- Python 3.9+
- pip

## Installation

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/your-username/todo-api.git
cd todo-api
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

### Using Docker

1. Build the Docker image:
```bash
docker build -t todo-api .
```

2. Run the container:
```bash
docker run -p 8000:8000 todo-api
```

## API Endpoints

### Base URL
```
http://localhost:8000
```

### Endpoints

#### Create Todo
```http
POST /todos/
Content-Type: application/json

{
    "title": "Buy groceries",
    "description": "Milk, eggs, bread"
}
```

Response: `201 Created`
```json
{
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "completed": false,
    "created_at": "2024-01-15T10:30:00",
    "updated_at": null
}
```

#### List All Todos
```http
GET /todos/
```

Response: `200 OK`
```json
[
    {
        "id": 1,
        "title": "Buy groceries",
        "description": "Milk, eggs, bread",
        "completed": false,
        "created_at": "2024-01-15T10:30:00",
        "updated_at": null
    }
]
```

#### Get Todo by ID
```http
GET /todos/{id}
```

Response: `200 OK` or `404 Not Found`

#### Update Todo
```http
PUT /todos/{id}
Content-Type: application/json

{
    "title": "Updated title",
    "completed": true
}
```

Response: `200 OK` or `404 Not Found`

#### Delete Todo
```http
DELETE /todos/{id}
```

Response: `200 OK` or `404 Not Found`

#### Health Check
```http
GET /health
```

Response: `200 OK`
```json
{
    "status": "healthy"
}
```

### Query Parameters

- `skip`: Number of items to skip (for pagination)
- `limit`: Maximum number of items to return (default: 100)

Example:
```http
GET /todos/?skip=0&limit=10
```

## API Documentation

Interactive API documentation is available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Testing

### Run Tests

```bash
pytest
```

### Run Tests with Coverage

```bash
pytest --cov=app --cov-report=html
```

This generates an HTML coverage report in the `htmlcov/` directory.

### Run Tests with Coverage and Fail if Below 90%

```bash
pytest --cov=app --cov-fail-under=90
```

## Project Structure

```
todo-api/
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI pipeline
├── app/
│   ├── __init__.py
│   ├── main.py                 # Application entry point
│   ├── database.py             # Database configuration
│   ├── models.py               # SQLAlchemy models
│   ├── schemas.py              # Pydantic schemas
│   ├── crud.py                 # CRUD operations
│   └── routes.py               # API routes
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # Pytest fixtures
│   ├── test_crud.py            # CRUD unit tests
│   └── test_api.py             # API integration tests
├── .coveragerc                 # Coverage configuration
├── pytest.ini                  # Pytest configuration
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Container definition
└── README.md                   # This file
```

## Technology Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **Pydantic**: Data validation using Python type annotations
- **SQLite**: Lightweight, file-based database
- **pytest**: Testing framework
- **httpx**: HTTP client for testing
- **uvicorn**: ASGI server

## CI/CD

The project uses GitHub Actions for continuous integration:

- Tests run on every push and pull request
- Tests run on Python 3.9, 3.10, and 3.11
- Coverage must be at least 90%
- Docker image is built and tested

## License

MIT License