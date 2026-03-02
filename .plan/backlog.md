# Project Backlog

## Summary
Build a REST API for a todo app using FastAPI and SQLite. The API will support CRUD operations (Create, Read, Update, Delete) for todo items. Each todo item will have an ID, title, description, and completed status. The project will include automated tests covering at least 90% of the code and a GitHub Actions CI pipeline to run tests on every commit.

## Assumptions
- Python 3.9+ will be used as the runtime
- SQLite will be used as the database (file-based, no external dependencies)
- SQLAlchemy ORM will be used for database operations
- Pytest will be used for testing with pytest-cov for coverage reporting
- The API will follow RESTful conventions
- No authentication is required for this MVP
- The application will run on port 8000 by default

## Epics

### EPIC-1: Core API Implementation

#### STORY-1.1: Project Setup and Dependencies
- **Priority**: P0
- **Phase**: implement
- **Description**: Set up the project structure, install dependencies, and configure the FastAPI application
- **Acceptance Criteria**:
  - [x] `requirements.txt` contains all necessary dependencies (fastapi, uvicorn, sqlalchemy, pytest, pytest-cov, httpx)
  - [x] Project has proper directory structure (app/, tests/, .github/)
  - [x] `main.py` creates and runs the FastAPI application
  - [x] Application starts successfully with `uvicorn`
- **Files**: requirements.txt, main.py, app/__init__.py
- **Status**: TODO

#### STORY-1.2: Database Models and Configuration
- **Priority**: P0
- **Phase**: implement
- **Description**: Create SQLAlchemy models for Todo items and database configuration
- **Acceptance Criteria**:
  - [x] `app/models.py` defines Todo model with id, title, description, completed fields
  - [x] `app/database.py` configures SQLite database connection
  - [x] Database tables are created on startup
  - [x] Todo model has proper column types and constraints
- **Files**: app/models.py, app/database.py
- **Status**: TODO

#### STORY-1.3: Pydantic Schemas
- **Priority**: P0
- **Phase**: implement
- **Description**: Create Pydantic schemas for request/response validation
- **Acceptance Criteria**:
  - [x] `app/schemas.py` defines TodoCreate, TodoUpdate, TodoResponse schemas
  - [x] TodoCreate schema requires title field
  - [x] TodoUpdate schema makes all fields optional
  - [x] TodoResponse includes all fields and id
- **Files**: app/schemas.py
- **Status**: TODO

#### STORY-1.4: CRUD Operations
- **Priority**: P0
- **Phase**: implement
- **Description**: Implement CRUD operations for Todo items
- **Acceptance Criteria**:
  - [x] `app/crud.py` contains functions for create, get, get_all, update, delete
  - [x] create_todo returns the created todo with generated id
  - [x] get_todo returns None if todo not found
  - [x] get_all_todos returns list of all todos
  - [x] update_todo returns updated todo or None if not found
  - [x] delete_todo returns True if deleted, False if not found
- **Files**: app/crud.py
- **Status**: TODO

#### STORY-1.5: API Routes
- **Priority**: P0
- **Phase**: implement
- **Description**: Create REST API endpoints for todo operations
- **Acceptance Criteria**:
  - [x] POST /todos - creates a new todo, returns 201 with todo data
  - [x] GET /todos - returns list of all todos with 200
  - [x] GET /todos/{id} - returns single todo with 200, or 404 if not found
  - [x] PUT /todos/{id} - updates todo with 200, or 404 if not found
  - [x] DELETE /todos/{id} - deletes todo with 200, or 404 if not found
  - [x] All endpoints follow REST conventions and return proper status codes
- **Files**: app/routes.py
- **Status**: TODO

### EPIC-2: Testing

#### STORY-2.1: Test Configuration and Fixtures
- **Priority**: P0
- **Phase**: test_auto
- **Description**: Set up pytest configuration and create test fixtures
- **Acceptance Criteria**:
  - [x] `pytest.ini` or `pyproject.toml` configures pytest
  - [x] `tests/conftest.py` contains test database fixture
  - [x] Test client fixture is created for API testing
  - [x] Tests use in-memory SQLite for isolation
- **Files**: pytest.ini, tests/conftest.py
- **Status**: TODO

#### STORY-2.2: CRUD Unit Tests
- **Priority**: P0
- **Phase**: test_auto
- **Description**: Write unit tests for CRUD operations
- **Acceptance Criteria**:
  - [x] Tests for create_todo function
  - [x] Tests for get_todo function (found and not found cases)
  - [x] Tests for get_all_todos function
  - [x] Tests for update_todo function (found and not found cases)
  - [x] Tests for delete_todo function (found and not found cases)
  - [x] All CRUD tests pass
- **Files**: tests/test_crud.py
- **Status**: TODO

#### STORY-2.3: API Endpoint Tests
- **Priority**: P0
- **Phase**: test_auto
- **Description**: Write integration tests for all API endpoints
- **Acceptance Criteria**:
  - [x] Test POST /todos with valid data returns 201
  - [x] Test POST /todos with missing title returns 422
  - [x] Test GET /todos returns list of todos
  - [x] Test GET /todos/{id} returns todo or 404
  - [x] Test PUT /todos/{id} updates todo or returns 404
  - [x] Test DELETE /todos/{id} deletes todo or returns 404
  - [x] All endpoint tests pass
- **Files**: tests/test_api.py
- **Status**: TODO

#### STORY-2.4: Test Coverage Configuration
- **Priority**: P1
- **Phase**: test_auto
- **Description**: Configure coverage to ensure 90%+ code coverage
- **Acceptance Criteria**:
  - [x] `.coveragerc` or coverage config in pyproject.toml
  - [x] Coverage report shows at least 90% coverage
  - [x] All source files are included in coverage
  - [x] Coverage can be run with `pytest --cov`
- **Files**: .coveragerc
- **Status**: TODO

### EPIC-3: CI/CD Pipeline

#### STORY-3.1: GitHub Actions Workflow
- **Priority**: P0
- **Phase**: cicd
- **Description**: Create GitHub Actions workflow for CI pipeline
- **Acceptance Criteria**:
  - [x] `.github/workflows/ci.yml` exists
  - [x] Workflow triggers on push and pull_request
  - [x] Workflow runs on Python 3.9+
  - [x] Workflow installs dependencies
  - [x] Workflow runs pytest with coverage
  - [x] Workflow fails if tests fail
- **Files**: .github/workflows/ci.yml
- **Status**: TODO

#### STORY-3.2: Docker Configuration
- **Priority**: P1
- **Phase**: cicd
- **Description**: Create Dockerfile for containerized deployment
- **Acceptance Criteria**:
  - [x] `Dockerfile` exists and builds successfully
  - [x] Dockerfile uses Python base image
  - [x] Dockerfile copies requirements and installs dependencies
  - [x] Dockerfile copies application code
  - [x] Dockerfile exposes port 8000
  - [x] Container runs with uvicorn
- **Files**: Dockerfile
- **Status**: TODO

### EPIC-4: Documentation

#### STORY-4.1: README Documentation
- **Priority**: P1
- **Phase**: validate
- **Description**: Create comprehensive README with usage instructions
- **Acceptance Criteria**:
  - [x] README.md describes the project
  - [x] README includes installation instructions
  - [x] README includes API endpoint documentation
  - [x] README includes example requests/responses
  - [x] README includes testing instructions
  - [x] README includes Docker usage instructions
- **Files**: README.md
- **Status**: TODO

## Non-Functional Requirements
- [ ] All tests pass (pytest)
- [ ] Docker build succeeds
- [ ] CI pipeline is green (GitHub Actions)
- [ ] No hardcoded secrets or credentials
- [ ] Error handling covers edge cases (404 for not found, 422 for validation errors)
- [ ] README is accurate and complete
- [ ] Test coverage is at least 90%