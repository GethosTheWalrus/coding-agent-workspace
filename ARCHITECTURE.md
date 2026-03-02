# Todo API Architecture

## Overview

This document describes the architecture of the Todo API, a RESTful web service built with FastAPI and SQLite for managing todo items.

## Technology Stack

- **Web Framework**: FastAPI 0.109.0
  - Auto-generated OpenAPI documentation
  - Async support
  - Built-in data validation with Pydantic
  
- **Database**: SQLite 3
  - Lightweight, file-based database
  - No separate server required
  - Perfect for this use case and easy deployment

- **ORM**: SQLAlchemy 2.0
  - Object-relational mapping
  - Database abstraction layer
  - Session management

- **Testing**: pytest 7.4 + pytest-cov 4.1
  - Comprehensive test framework
  - Coverage reporting
  - Fixtures for test isolation

- **Container**: Docker
  - Consistent deployment environment
  - Multi-stage builds for smaller images
  - Non-root user for security

## Directory Structure

```
todo-api/
├── .github/
│   └── workflows/
│       └── ci.yml          # CI/CD pipeline configuration
├── app/
│   ├── __init__.py         # Package initialization
│   ├── main.py             # FastAPI application entry point
│   ├── config.py           # Application configuration
│   ├── database.py         # Database connection and session management
│   ├── models.py           # SQLAlchemy ORM models
│   ├── schemas.py          # Pydantic request/response schemas
│   ├── crud.py             # CRUD operations
│   └── routes.py           # API route definitions
├── tests/
│   ├── __init__.py         # Test package initialization
│   ├── conftest.py         # Pytest fixtures
│   ├── test_crud.py        # CRUD unit tests
│   └── test_api.py         # API integration tests
├── .gitignore              # Git ignore rules
├── Dockerfile              # Container configuration
├── pytest.ini              # Pytest configuration
├── requirements.txt        # Python dependencies
├── ARCHITECTURE.md         # This file
└── README.md               # Project documentation
```

## Component Architecture

### 1. Application Layer (`app/main.py`)

The entry point that creates and configures the FastAPI application:
- Configures CORS middleware
- Includes API routes
- Sets up startup events for database initialization
- Provides root and health check endpoints

### 2. Configuration Layer (`app/config.py`)

Manages application settings:
- Loads environment variables
- Provides database URL configuration
- Supports different environments (dev, test, prod)

### 3. Data Layer

#### Database Configuration (`app/database.py`)
- Creates SQLAlchemy engine
- Manages database sessions
- Provides `get_db()` dependency for route functions
- Handles database initialization

#### Models (`app/models.py`)
- Defines SQLAlchemy ORM models
- `Todo` model with fields:
  - `id`: Integer, primary key
  - `title`: String(255), required
  - `description`: String(1000), optional
  - `completed`: Boolean, default False
  - `created_at`: DateTime, auto-generated
  - `updated_at`: DateTime, auto-updated

### 4. Schema Layer (`app/schemas.py`)

Pydantic schemas for request/response validation:
- `TodoBase`: Base schema with common fields
- `TodoCreate`: Schema for creating todos
- `TodoUpdate`: Schema for updating todos (all fields optional)
- `TodoResponse`: Schema for API responses (includes id and timestamps)
- `TodoListResponse`: Schema for paginated list responses

### 5. Business Logic Layer (`app/crud.py`)

CRUD operations for todo items:
- `create_todo()`: Create a new todo
- `get_todo()`: Retrieve a single todo by ID
- `get_todos()`: List todos with pagination and filtering
- `update_todo()`: Update an existing todo
- `delete_todo()`: Delete a todo
- `get_todo_count()`: Get total count of todos

### 6. API Layer (`app/routes.py`)

REST API endpoints:
- `POST /todos` - Create a new todo (201)
- `GET /todos` - List all todos (200)
- `GET /todos/{todo_id}` - Get a specific todo (200/404)
- `PUT /todos/{todo_id}` - Update a todo (200/404)
- `DELETE /todos/{todo_id}` - Delete a todo (204/404)
- `GET /` - Root endpoint with API info
- `GET /health` - Health check endpoint

## API Design

### Request/Response Patterns

**Create Todo**
```http
POST /todos
Content-Type: application/json

{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": false
}

Response: 201 Created
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": false,
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": null
}
```

**List Todos**
```http
GET /todos?skip=0&limit=10&completed=false

Response: 200 OK
{
  "items": [...],
  "total": 10,
  "page": 1,
  "page_size": 10
}
```

**Update Todo**
```http
PUT /todos/1
Content-Type: application/json

{
  "completed": true
}

Response: 200 OK
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "completed": true,
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-01T01:00:00Z"
}
```

**Delete Todo**
```http
DELETE /todos/1

Response: 204 No Content
```

### Error Handling

- **400 Bad Request**: Invalid request body (Pydantic validation)
- **404 Not Found**: Resource doesn't exist
- **500 Internal Server Error**: Unexpected server errors

## Testing Strategy

### Unit Tests (`tests/test_crud.py`)
- Test individual CRUD functions
- Test with mock database sessions
- Cover edge cases and error conditions

### Integration Tests (`tests/test_api.py`)
- Test full API endpoints
- Use TestClient for HTTP requests
- Verify request/response cycles
- Test error responses

### Test Coverage
- Target: 90% code coverage
- Enforced via pytest-cov
- CI pipeline fails if coverage drops below 90%

## CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/ci.yml`) includes:

1. **Test Job**: Runs pytest with coverage
2. **Build Job**: Builds and validates Docker image
3. **Lint Job**: Runs flake8, black, and mypy

All jobs run on push to main and pull requests.

## Security Considerations

- Non-root user in Docker container
- No hardcoded secrets
- Environment-based configuration
- CORS middleware configured for flexibility

## Deployment

### Local Development
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Docker
```bash
docker build -t todo-api .
docker run -p 8000:8000 todo-api
```

### Environment Variables
- `DATABASE_URL`: Database connection string (default: `sqlite:///./todo.db`)
- `APP_NAME`: Application name (default: "Todo API")
- `DEBUG`: Enable debug mode (default: false)