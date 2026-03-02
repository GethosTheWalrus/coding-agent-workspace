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
  - [ ] requirements.txt exists with fastapi, uvicorn, sqlalchemy, pydantic, pytest, pytest-cov
  - [ ] Project has src/ directory structure with app/ subdirectory
  - [ ] __init__.py files are in place for all packages
- **Files**: requirements.txt, src/__init__.py, src/app/__init__.py
- **Status**: TODO

#### STORY-1.2: Database Models and Configuration
- **Priority**: P0
- **Phase**: implement
- **Description**: Create SQLAlchemy models for Todo items and configure database connection with SQLite
- **Acceptance Criteria**:
  - [ ] Todo model has id (integer, primary key), title (string), description (string), completed (boolean)
  - [ ] Database engine is configured to use SQLite
  - [ ] Database tables are created on startup
  - [ ] Database session management is implemented
- **Files**: src/app/models.py, src/app/database.py
- **Status**: TODO

#### STORY-1.3: Pydantic Schemas for Request/Response
- **Priority**: P0
- **Phase**: implement
- **Description**: Create Pydantic schemas for todo item validation and serialization
- **Acceptance Criteria**:
  - [ ] TodoCreate schema for creating todos (title, description, completed optional)
  - [ ] TodoUpdate schema for updating todos (all fields optional)
  - [ ] TodoResponse schema for returning todo items (includes id)
  - [ ] Schemas include proper field validation (title required, max length constraints)
- **Files**: src/app/schemas.py
- **Status**: TODO

#### STORY-1.4: CRUD Operations
- **Priority**: P0
- **Phase**: implement
- **Description**: Implement CRUD operations for todo items using SQLAlchemy
- **Acceptance Criteria**:
  - [ ] create_todo function creates and returns a new todo
  - [ ] get_todos function retrieves all todos with optional filtering
  - [ ] get_todo function retrieves a single todo by ID
  - [ ] update_todo function updates an existing todo
  - [ ] delete_todo function removes a todo by ID
  - [ ] All functions handle database sessions properly
- **Files**: src/app/crud.py
- **Status**: TODO

#### STORY-1.5: API Routes/Endpoints
- **Priority**: P0
- **Phase**: implement
- **Description**: Create FastAPI routes for all CRUD operations
- **Acceptance Criteria**:
  - [ ] POST /todos - Create a new todo, returns 201 on success, 422 on validation error
  - [ ] GET /todos - List all todos, returns 200 with array of todos
  - [ ] GET /todos/{todo_id} - Get single todo, returns 200 or 404
  - [ ] PUT /todos/{todo_id} - Update todo, returns 200 or 404
  - [ ] DELETE /todos/{todo_id} - Delete todo, returns 204 or 404
  - [ ] All endpoints return proper HTTP status codes
  - [ ] Error responses include meaningful error messages
- **Files**: src/app/main.py, src/app/routes.py
- **Status**: TODO

### EPIC-2: Testing

#### STORY-2.1: Test Fixtures and Setup
- **Priority**: P0
- **Phase**: test_auto
- **Description**: Create test fixtures, conftest.py, and test database setup
- **Acceptance Criteria**:
  - [ ] conftest.py defines test database fixtures
  - [ ] Test database uses in-memory SQLite for isolation
  - [ ] Fixtures provide clean database state for each test
  - [ ] Test client is configured for FastAPI testing
- **Files**: tests/__init__.py, tests/conftest.py
- **Status**: TODO

#### STORY-2.2: Test CRUD Operations
- **Priority**: P0
- **Phase**: test_auto
- **Description**: Write unit tests for CRUD operations
- **Acceptance Criteria**:
  - [ ] Test create_todo creates a todo with correct data
  - [ ] Test get_todos returns all todos
  - [ ] Test get_todo returns single todo or None
  - [ ] Test update_todo modifies existing todo
  - [ ] Test delete_todo removes todo from database
  - [ ] Tests cover edge cases (empty database, non-existent IDs)
- **Files**: tests/test_crud.py
- **Status**: TODO

#### STORY-2.3: Test API Endpoints
- **Priority**: P0
- **Phase**: test_auto
- **Description**: Write integration tests for all API endpoints
- **Acceptance Criteria**:
  - [ ] Test POST /todos creates todo and returns 201
  - [ ] Test POST /todos with invalid data returns 422
  - [ ] Test GET /todos returns list of todos
  - [ ] Test GET /todos/{id} returns todo or 404
  - [ ] Test PUT /todos/{id} updates todo or returns 404
  - [ ] Test DELETE /todos/{id} deletes todo or returns 404
  - [ ] Test response payloads match schema definitions
- **Files**: tests/test_api.py
- **Status**: TODO

#### STORY-2.4: Achieve 90% Code Coverage
- **Priority**: P1
- **Phase**: test_auto
- **Description**: Ensure all code paths are tested to achieve 90%+ coverage
- **Acceptance Criteria**:
  - [ ] pytest-cov reports 90% or higher coverage
  - [ ] All branches in CRUD operations are tested
  - [ ] Error handling paths are tested
  - [ ] Coverage report is generated and visible
- **Files**: tests/ (existing test files)
- **Status**: TODO

### EPIC-3: CI/CD Pipeline

#### STORY-3.1: GitHub Actions Workflow
- **Priority**: P0
- **Phase**: cicd
- **Description**: Create GitHub Actions workflow to run tests on every push
- **Acceptance Criteria**:
  - [ ] Workflow file exists at .github/workflows/ci.yml
  - [ ] Workflow triggers on push to main branch
  - [ ] Workflow triggers on pull requests
  - [ ] Job runs on Ubuntu latest
  - [ ] Job sets up Python 3.10+
  - [ ] Job installs dependencies from requirements.txt
  - [ ] Job runs pytest with coverage
  - [ ] Job fails if tests fail or coverage < 90%
- **Files**: .github/workflows/ci.yml
- **Status**: TODO

### EPIC-4: Documentation and Configuration

#### STORY-4.1: README Documentation
- **Priority**: P1
- **Phase**: implement
- **Description**: Create comprehensive README with setup instructions and API documentation
- **Acceptance Criteria**:
  - [ ] README.md exists with project description
  - [ ] Installation instructions are provided
  - [ ] API endpoints are documented with examples
  - [ ] Running tests instructions are included
  - [ ] Example curl commands are provided for each endpoint
- **Files**: README.md
- **Status**: TODO

#### STORY-4.2: Application Configuration
- **Priority**: P1
- **Phase**: implement
- **Description**: Add configuration management for database URL and other settings
- **Acceptance Criteria**:
  - [ ] Config class reads from environment variables
  - [ ] Default database URL is SQLite
  - [ ] Configuration is accessible throughout the app
- **Files**: src/app/config.py
- **Status**: TODO

## Non-Functional Requirements
- [ ] All tests pass
- [ ] Docker build succeeds (if Docker is used)
- [ ] CI pipeline is green
- [ ] No hardcoded secrets or credentials
- [ ] Error handling covers edge cases
- [ ] README is accurate and complete
- [ ] Code coverage is at least 90%
- [ ] FastAPI auto-generated docs work ( /docs endpoint)