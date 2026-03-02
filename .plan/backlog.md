# Project Backlog

## Summary
Build a REST API for a todo application using FastAPI and SQLite. The API will support CRUD operations (Create, Read, Update, Delete) for todo items. Each todo item will have an ID, title, description, and completed status. The project will include automated tests covering at least 90% of the code and a GitHub Actions CI pipeline to run tests on every push.

## Assumptions
- Python 3.10+ will be used as the runtime
- SQLite will be used as the database (file-based, no external server needed)
- FastAPI will be the web framework with Pydantic for data validation
- pytest will be used for testing with pytest-cov for coverage reporting
- The API will run on port 8000 by default
- No authentication is required for this MVP
- The database file will be named `todos.db` and stored in the project root

## Epics

### EPIC-1: Core API Implementation

#### STORY-1.1: Project Setup and Dependencies
- **Priority**: P0
- **Phase**: implement
- **Description**: Set up the project structure, create requirements.txt with all dependencies, and configure the basic project layout
- **Acceptance Criteria**:
  - [x] requirements.txt exists with fastapi, uvicorn, sqlalchemy, pydantic, pytest, pytest-cov
  - [x] Project has src/ directory structure with app/ subdirectory
  - [x] __init__.py files are in place for all packages
- **Files**: requirements.txt, src/__init__.py, src/app/__init__.py
- **Status**: DONE

#### STORY-1.2: Database Models and Configuration
- **Priority**: P0
- **Phase**: implement
- **Description**: Create SQLAlchemy models for Todo items and configure database connection with SQLite
- **Acceptance Criteria**:
  - [x] Todo model has id (integer, primary key), title (string), description (string), completed (boolean)
  - [x] Database engine is configured to use SQLite
  - [x] Database tables are created on startup
  - [x] Database session management is implemented
- **Files**: src/app/models.py, src/app/database.py
- **Status**: DONE

#### STORY-1.3: Pydantic Schemas for Request/Response
- **Priority**: P0
- **Phase**: implement
- **Description**: Create Pydantic schemas for todo item validation and serialization
- **Acceptance Criteria**:
  - [x] TodoCreate schema for creating todos (title, description, completed optional)
  - [x] TodoUpdate schema for updating todos (all fields optional)
  - [x] TodoResponse schema for returning todo items (includes id)
  - [x] Schemas include proper field validation (title required, max length constraints)
- **Files**: src/app/schemas.py
- **Status**: DONE

#### STORY-1.4: CRUD Operations
- **Priority**: P0
- **Phase**: implement
- **Description**: Implement CRUD operations for todo items using SQLAlchemy
- **Acceptance Criteria**:
  - [x] create_todo function creates and returns a new todo
  - [x] get_todos function retrieves all todos with optional filtering
  - [x] get_todo function retrieves a single todo by ID
  - [x] update_todo function updates an existing todo
  - [x] delete_todo function removes a todo by ID
  - [x] All functions handle database sessions properly
- **Files**: src/app/crud.py
- **Status**: DONE

#### STORY-1.5: API Routes/Endpoints
- **Priority**: P0
- **Phase**: implement
- **Description**: Create FastAPI routes for all CRUD operations
- **Acceptance Criteria**:
  - [x] POST /todos - Create a new todo, returns 201 on success, 422 on validation error
  - [x] GET /todos - List all todos, returns 200 with array of todos
  - [x] GET /todos/{todo_id} - Get single todo, returns 200 or 404
  - [x] PUT /todos/{todo_id} - Update todo, returns 200 or 404
  - [x] DELETE /todos/{todo_id} - Delete todo, returns 204 or 404
  - [x] All endpoints return proper HTTP status codes
  - [x] Error responses include meaningful error messages
- **Files**: src/app/main.py, src/app/routes.py
- **Status**: DONE

### EPIC-2: Testing

#### STORY-2.1: Test Fixtures and Setup
- **Priority**: P0
- **Phase**: test_auto
- **Description**: Create test fixtures, conftest.py, and test database setup
- **Acceptance Criteria**:
  - [x] conftest.py defines test database fixtures
  - [x] Test database uses in-memory SQLite for isolation
  - [x] Fixtures provide clean database state for each test
  - [x] Test client is configured for FastAPI testing
- **Files**: tests/__init__.py, tests/conftest.py
- **Status**: DONE

#### STORY-2.2: Test CRUD Operations
- **Priority**: P0
- **Phase**: test_auto
- **Description**: Write unit tests for CRUD operations
- **Acceptance Criteria**:
  - [x] Test create_todo creates a todo with correct data
  - [x] Test get_todos returns all todos
  - [x] Test get_todo returns single todo or None
  - [x] Test update_todo modifies existing todo
  - [x] Test delete_todo removes todo from database
  - [x] Tests cover edge cases (empty database, non-existent IDs)
- **Files**: tests/test_crud.py
- **Status**: DONE

#### STORY-2.3: Test API Endpoints
- **Priority**: P0
- **Phase**: test_auto
- **Description**: Write integration tests for all API endpoints
- **Acceptance Criteria**:
  - [x] Test POST /todos creates todo and returns 201
  - [x] Test POST /todos with invalid data returns 422
  - [x] Test GET /todos returns list of todos
  - [x] Test GET /todos/{id} returns todo or 404
  - [x] Test PUT /todos/{id} updates todo or returns 404
  - [x] Test DELETE /todos/{id} deletes todo or returns 404
  - [x] Test response payloads match schema definitions
- **Files**: tests/test_api.py
- **Status**: DONE

#### STORY-2.4: Achieve 90% Code Coverage
- **Priority**: P1
- **Phase**: test_auto
- **Description**: Ensure all code paths are tested to achieve 90%+ coverage
- **Acceptance Criteria**:
  - [x] pytest-cov reports 90% or higher coverage (96% achieved)
  - [x] All branches in CRUD operations are tested
  - [x] Error handling paths are tested
  - [x] Coverage report is generated and visible
- **Files**: tests/ (existing test files)
- **Status**: DONE

### EPIC-3: CI/CD Pipeline

#### STORY-3.1: GitHub Actions Workflow
- **Priority**: P0
- **Phase**: cicd
- **Description**: Create GitHub Actions workflow to run tests on every push
- **Acceptance Criteria**:
  - [x] Workflow file exists at .github/workflows/ci.yml
  - [x] Workflow triggers on push to main branch
  - [x] Workflow triggers on pull requests
  - [x] Job runs on Ubuntu latest
  - [x] Job sets up Python 3.10+
  - [x] Job installs dependencies from requirements.txt
  - [x] Job runs pytest with coverage
  - [x] Job fails if tests fail or coverage < 90%
- **Files**: .github/workflows/ci.yml
- **Status**: DONE

### EPIC-4: Documentation and Configuration

#### STORY-4.1: README Documentation
- **Priority**: P1
- **Phase**: implement
- **Description**: Create comprehensive README with setup instructions and API documentation
- **Acceptance Criteria**:
  - [x] README.md exists with project description
  - [x] Installation instructions are provided
  - [x] API endpoints are documented with examples
  - [x] Running tests instructions are included
  - [x] Example curl commands are provided for each endpoint
- **Files**: README.md
- **Status**: DONE

#### STORY-4.2: Application Configuration
- **Priority**: P1
- **Phase**: implement
- **Description**: Add configuration management for database URL and other settings
- **Acceptance Criteria**:
  - [x] Config class reads from environment variables
  - [x] Default database URL is SQLite
  - [x] Configuration is accessible throughout the app
- **Files**: src/app/config.py
- **Status**: DONE

## Non-Functional Requirements
- [x] All tests pass (29 tests)
- [x] Code coverage is at least 90% (96% achieved)
- [x] FastAPI auto-generated docs work (/docs endpoint)
- [x] No hardcoded secrets or credentials
- [x] Error handling covers edge cases
- [x] README is accurate and complete