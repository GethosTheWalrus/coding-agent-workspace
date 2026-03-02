# Todo API Architecture Design

## Overview

This document describes the architecture for a REST API todo application built with FastAPI and SQLite.

## Technology Stack

| Component | Technology | Rationale |
|-----------|------------|-----------|
| Framework | FastAPI | Modern, fast, automatic OpenAPI docs, type validation |
| Database | SQLite | Simple, file-based, no external dependencies |
| ORM | SQLAlchemy | Robust ORM, async support, database abstraction |
| Validation | Pydantic | Data validation, serialization, type hints |
| Testing | pytest + httpx | Industry standard, async support, easy mocking |
| Coverage | pytest-cov | Coverage reporting |
| Server | uvicorn | ASGI server for FastAPI |
| CI/CD | GitHub Actions | Native GitHub integration |
| Containerization | Docker | Consistent deployment |

## Directory Structure

```
todo-api/
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI pipeline
├── app/
│   ├── __init__.py             # Package marker
│   ├── main.py                 # Application entry point
│   ├── database.py             # Database configuration and session
│   ├── models.py               # SQLAlchemy ORM models
│   ├── schemas.py              # Pydantic schemas for validation
│   ├── crud.py                 # CRUD operations
│   └── routes.py               # API route definitions
├── tests/
│   ├── __init__.py             # Package marker
│   ├── conftest.py             # Pytest fixtures
│   ├── test_crud.py            # CRUD unit tests
│   └── test_api.py             # API integration tests
├── .coveragerc                 # Coverage configuration
├── pytest.ini                  # Pytest configuration
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Container definition
├── README.md                   # Project documentation
└── docs/
    └── design.md               # This design document
```

## Data Models

### Todo Model (SQLAlchemy)

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Integer | Primary Key, Auto-increment | Unique identifier |
| title | String(255) | Not Null | Todo title |
| description | Text | Nullable | Detailed description |
| completed | Boolean | Default False | Completion status |
| created_at | DateTime | Not Null, Auto | Creation timestamp |
| updated_at | DateTime | Nullable, Auto | Last update timestamp |

### Database Schema

```sql
CREATE TABLE todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT 0,
    created_at DATETIME NOT NULL,
    updated_at DATETIME
);
```

## API Schemas (Pydantic)

### TodoCreate
```json
{
    "title": "string (required, max 255 chars)",
    "description": "string (optional)"
}
```

### TodoUpdate
```json
{
    "title": "string (optional)",
    "description": "string (optional)",
    "completed": "boolean (optional)"
}
```

### TodoResponse
```json
{
    "id": "integer",
    "title": "string",
    "description": "string | null",
    "completed": "boolean",
    "created_at": "ISO 8601 datetime",
    "updated_at": "ISO 8601 datetime | null"
}
```

## API Endpoints

| Method | Endpoint | Description | Status Codes |
|--------|----------|-------------|--------------|
| POST | /todos | Create a new todo | 201 Created, 422 Validation Error |
| GET | /todos | List all todos | 200 OK |
| GET | /todos/{id} | Get a specific todo | 200 OK, 404 Not Found |
| PUT | /todos/{id} | Update a todo | 200 OK, 404 Not Found |
| DELETE | /todos/{id} | Delete a todo | 200 OK, 404 Not Found |

### Request/Response Examples

#### Create Todo
```http
POST /todos
Content-Type: application/json

{
    "title": "Buy groceries",
    "description": "Milk, eggs, bread"
}

Response: 201 Created
{
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "completed": false,
    "created_at": "2024-01-15T10:30:00",
    "updated_at": null
}
```

#### Get All Todos
```http
GET /todos

Response: 200 OK
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
GET /todos/1

Response: 200 OK
{
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "completed": false,
    "created_at": "2024-01-15T10:30:00",
    "updated_at": null
}
```

#### Update Todo
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
    "created_at": "2024-01-15T10:30:00",
    "updated_at": "2024-01-15T11:00:00"
}
```

#### Delete Todo
```http
DELETE /todos/1

Response: 200 OK
{
    "message": "Todo deleted successfully"
}
```

## Component Architecture

### Layered Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    API Layer (routes.py)                │
│  - HTTP request handling                                │
│  - Request validation (Pydantic)                        │
│  - Response formatting                                  │
│  - Status code management                               │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│                   CRUD Layer (crud.py)                  │
│  - Business logic for data operations                   │
│  - Database transaction management                      │
│  - Data transformation                                  │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│                  Data Layer (models.py)                 │
│  - SQLAlchemy ORM models                                │
│  - Database schema definitions                          │
│  - Relationship mappings                                │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│              Database Configuration (database.py)       │
│  - SQLite connection management                         │
│  - Session factory                                      │
│  - Table creation                                       │
└─────────────────────────────────────────────────────────┘
```

## Module Responsibilities

### app/main.py
- Application factory function
- Middleware configuration
- CORS setup (if needed)
- Startup/shutdown events
- Server entry point

### app/database.py
- SQLite database URL configuration
- SQLAlchemy engine creation
- SessionLocal session factory
- Base class for declarative models
- Database initialization

### app/models.py
- Todo SQLAlchemy model
- Column definitions and constraints
- Table name and relationships
- String representation

### app/schemas.py
- TodoCreate: Input schema for creating todos
- TodoUpdate: Input schema for updating todos
- TodoResponse: Output schema for todo data
- Validation rules and defaults

### app/crud.py
- create_todo(session, todo_data) -> Todo
- get_todo(session, todo_id) -> Todo | None
- get_all_todos(session) -> List[Todo]
- update_todo(session, todo_id, todo_data) -> Todo | None
- delete_todo(session, todo_id) -> bool

### app/routes.py
- POST /todos: create_todo_endpoint
- GET /todos: list_todos_endpoint
- GET /todos/{id}: get_todo_endpoint
- PUT /todos/{id}: update_todo_endpoint
- DELETE /todos/{id}: delete_todo_endpoint

## Testing Strategy

### Test Fixtures (tests/conftest.py)
- `test_db`: In-memory SQLite database
- `db_session`: Database session fixture
- `client`: TestClient for API testing
- `sample_todo`: Sample todo data fixture

### Test Coverage Goals
- CRUD operations: 100% coverage
- API endpoints: 100% coverage
- Error handling: All edge cases covered
- Validation: All schema validations tested

### Test Categories
1. **Unit Tests** (test_crud.py)
   - Test each CRUD function independently
   - Mock database session where appropriate
   - Test edge cases (not found, validation)

2. **Integration Tests** (test_api.py)
   - Test full API endpoints
   - Test HTTP status codes
   - Test request/response formats
   - Test error responses

## CI/CD Pipeline

### GitHub Actions Workflow
1. Trigger on push and pull_request
2. Set up Python 3.9+
3. Install dependencies
4. Run tests with coverage
5. Fail if coverage < 90%
6. Report coverage results

### Docker Configuration
- Multi-stage build for smaller image
- Non-root user for security
- Health check configuration
- Port 8000 exposed

## Error Handling

### HTTP Status Codes
- 200: Success
- 201: Created
- 404: Resource not found
- 422: Validation error (FastAPI default)
- 500: Internal server error

### Error Response Format
```json
{
    "detail": "Error message"
}
```

## Security Considerations
- No authentication required for MVP
- Input validation via Pydantic
- SQL injection prevention via SQLAlchemy ORM
- No sensitive data in logs

## Future Enhancements
- Authentication and authorization
- Pagination for list endpoints
- Filtering and sorting
- Soft delete
- Background tasks
- Async database operations
- Redis caching
- API versioning