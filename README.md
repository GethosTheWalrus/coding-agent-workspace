# Todo API

A REST API for a todo application built with FastAPI and SQLite.

## Features

- Create, read, update, and delete todo items
- Automatic OpenAPI documentation at `/docs`
- SQLite database for simple file-based storage
- Automated tests with 90%+ code coverage
- CI/CD pipeline with GitHub Actions
- Docker support for containerized deployment

## Requirements

- Python 3.10+
- pip
- Docker (optional, for containerized deployment)

## Installation

### Option 1: Local Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd todo-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Option 2: Docker

Build and run using Docker:
```bash
docker build -t todo-api .
docker run -p 8000:8000 todo-api
```

Or use docker-compose:
```bash
docker-compose up -d
```

## Running the Application

### Local Development

Start the development server:
```bash
uvicorn src.app.main:app --reload
```

The API will be available at `http://localhost:8000`.

### Docker

Run the production container:
```bash
docker run -p 8000:8000 todo-api:prod
```

### Docker Compose

Start all services:
```bash
docker-compose up -d
```

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

### Local Tests

Run all tests with coverage:
```bash
pytest --cov=src/app --cov-report=term-missing -v
```

Run tests with coverage report in HTML:
```bash
pytest --cov=src/app --cov-report=html -v
```

### Docker Tests

Run tests inside a Docker container:
```bash
docker build -t todo-api:test --target test-runner .
docker run --rm todo-api:test
```

Or using docker-compose:
```bash
docker-compose run --rm test
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
├── .dockerignore           # Docker ignore file
├── .env.example            # Environment variables template
├── Dockerfile              # Multi-stage Docker build
├── docker-compose.yml      # Docker Compose configuration
├── requirements.txt        # Dependencies
└── README.md              # This file
```

## Configuration

Environment variables:
- `DATABASE_URL` - Database connection string (default: `sqlite:///todos.db`)
- `DEBUG` - Enable debug mode (default: `false`)
- `HOST` - Server host (default: `0.0.0.0`)
- `PORT` - Server port (default: `8000`)

Copy `.env.example` to `.env` and customize as needed.

## CI/CD

The project uses GitHub Actions for continuous integration:

- Tests run on every push to `main` branch
- Tests run on every pull request
- Code coverage must be at least 90%
- Coverage reports are uploaded to Codecov

## License

MIT