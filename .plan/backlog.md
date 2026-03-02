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
  - [ ] `requirements.txt` contains all necessary dependencies (fastapi, uvicorn, sqlalchemy, pytest, pytest-cov, httpx)
  - [ ] Project has proper directory structure (app/, tests/, .github/)
  - [ ] `main.py` creates and runs the FastAPI application
  - [ ] Application starts successfully with `uvicorn`
- **Files**: requirements.txt, main.py, app/__init__.py
- **Status**: TODO

#### STORY-1.2: Database Models and Configuration
- **Priority**: P0
- **Phase**: implement
- **Description**: Create SQLAlchemy models for Todo items and database configuration
- **Acceptance Criteria**:
  - [ ] `app/models.py` defines Todo model with id, title, description, completed fields
  - [ ] `app/database.py` configures SQLite database connection
  - [ ] Database tables are created on startup
  - [ ] Todo model has proper column types and constraints
- **Files**: app/models.py, app/database.py
- **Status**: TODO

#### STORY-1.3: Pydantic Schemas
- **Priority**: P0
- **Phase**: implement
- **Description**: Create Pydantic schemas for request/response validation
- **Acceptance Criteria**:
  - [ ] `app/schemas.py` defines TodoCreate, TodoUpdate, TodoResponse schemas
  - [ ] TodoCreate schema requires title field
  - [ ] TodoUpdate schema makes all fields optional
  - [ ] TodoResponse includes all fields and id
- **Files**: app/schemas.py
- **Status**: TODO

#### STORY-1.4: CRUD Operations
- **Priority**: P0
- **Phase**: implement
- **Description**: Implement CRUD operations for Todo items
- **Acceptance Criteria**:
  - [ ] `app/crud.py` contains functions for create, get, get_all, update, delete
  - [ ] create_todo returns the created todo with generated id
  - [ ] get_todo returns None if todo not found
  - [ ] get_all_todos returns list of all todos
  - [ ] update_todo returns updated todo or None if not found
  - [ ] delete_todo returns True if deleted, False if not found
- **Files**: app/crud.py
- **Status**: TODO

#### STORY-1.5: API Routes
- **Priority**: P0
- **Phase**: implement
- **Description**: Create REST API endpoints for todo operations
- **Acceptance Criteria**:
  - [ ] POST /todos - creates a new todo, returns 201 with todo data
  - [ ] GET /todos - returns list of all todos with 200
  - [ ] GET /todos/{id} - returns single todo with 200, or 404 if not found
  - [ ] PUT /todos/{id} - updates todo with 200, or 404 if not found
  - [ ] DELETE /todos/{id} - deletes todo with 200, or 404 if not found
  - [ ] All endpoints follow REST conventions and return proper status codes
- **Files**: app/routes.py
- **Status**: TODO

### EPIC-2: Testing

#### STORY-2.1: Test Configuration and Fixtures
- **Priority**: P0
- **Phase**: test_auto
- **Description**: Set up pytest configuration and create test fixtures
- **Acceptance Criteria**:
  - [ ] `pytest.ini` or `pyproject.toml` configures pytest
  - [ ] `tests/conftest.py` contains test database fixture
  - [ ] Test client fixture is created for API testing
  - [ ] Tests use in-memory SQLite for isolation
- **Files**: pytest.ini, tests/conftest.py
- **Status**: TODO

#### STORY-2.2: CRUD Unit Tests
- **Priority**: P0
- **Phase**: test_auto
- **Description**: Write unit tests for CRUD operations
- **Acceptance Criteria**:
  - [ ] Tests for create_todo function
  - [ ] Tests for get_todo function (found and not found cases)
  - [ ] Tests for get_all_todos function
  - [ ] Tests for update_todo function (found and not found cases)
  - [ ] Tests for delete_todo function (found and not found cases)
  - [ ] All CRUD tests pass
- **Files**: tests/test_crud.py
- **Status**: TODO

#### STORY-2.3: API Endpoint Tests
- **Priority**: P0
- **Phase**: test_auto
- **Description**: Write integration tests for all API endpoints
- **Acceptance Criteria**:
  - [ ] Test POST /todos with valid data returns 201
  - [ ] Test POST /todos with missing title returns 422
  - [ ] Test GET /todos returns list of todos
  - [ ] Test GET /todos/{id} returns todo or 404
  - [ ] Test PUT /todos/{id} updates todo or returns 404
  - [ ] Test DELETE /todos/{id} deletes todo or returns 404
  - [ ] All endpoint tests pass
- **Files**: tests/test_api.py
- **Status**: TODO

#### STORY-2.4: Test Coverage Configuration
- **Priority**: P1
- **Phase**: test_auto
- **Description**: Configure coverage to ensure 90%+ code coverage
- **Acceptance Criteria**:
  - [ ] `.coveragerc` or coverage config in pyproject.toml
  - [ ] Coverage report shows at least 90% coverage
  - [ ] All source files are included in coverage
  - [ ] Coverage can be run with `pytest --cov`
- **Files**: .coveragerc
- **Status**: TODO

### EPIC-3: CI/CD Pipeline

#### STORY-3.1: GitHub Actions Workflow
- **Priority**: P0
- **Phase**: cicd
- **Description**: Create GitHub Actions workflow for CI pipeline
- **Acceptance Criteria**:
  - [ ] `.github/workflows/ci.yml` exists
  - [ ] Workflow triggers on push and pull_request
  - [ ] Workflow runs on Python 3.9+
  - [ ] Workflow installs dependencies
  - [ ] Workflow runs pytest with coverage
  - [ ] Workflow fails if tests fail
- **Files**: .github/workflows/ci.yml
- **Status**: TODO

#### STORY-3.2: Docker Configuration
- **Priority**: P1
- **Phase**: cicd
- **Description**: Create Dockerfile for containerized deployment
- **Acceptance Criteria**:
  - [ ] `Dockerfile` exists and builds successfully
  - [ ] Dockerfile uses Python base image
  - [ ] Dockerfile copies requirements and installs dependencies
  - [ ] Dockerfile copies application code
  - [ ] Dockerfile exposes port 8000
  - [ ] Container runs with uvicorn
- **Files**: Dockerfile
- **Status**: TODO

### EPIC-4: Documentation

#### STORY-4.1: README Documentation
- **Priority**: P1
- **Phase**: validate
- **Description**: Create comprehensive README with usage instructions
- **Acceptance Criteria**:
  - [ ] README.md describes the project
  - [ ] README includes installation instructions
  - [ ] README includes API endpoint documentation
  - [ ] README includes example requests/responses
  - [ ] README includes testing instructions
  - [ ] README includes Docker usage instructions
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