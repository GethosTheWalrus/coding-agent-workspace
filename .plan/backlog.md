# Project Backlog

## Summary
Build a REST API for a todo application using FastAPI and SQLite. The API will support CRUD operations (Create, Read, Update, Delete) for todo items. Each todo item will have an ID, title, description, and completed status. The project will include automated tests covering at least 90% of the code and a GitHub Actions CI pipeline to run tests on each push.

## Assumptions
- The API will use SQLite as the database for simplicity and portability
- FastAPI will be used for the web framework due to its built-in OpenAPI documentation and async support
- Pytest will be used for automated testing
- The CI pipeline will run on push to main and pull requests
- No authentication is required for this MVP
- The application will be containerized using Docker for consistent deployment

## Epics

### EPIC-1: Core API Implementation

#### STORY-1.1: Project Setup and Configuration
- **Priority**: P0
- **Phase**: design
- **Description**: Set up the project structure, dependencies, and configuration files
- **Acceptance Criteria**:
  - [x] requirements.txt file exists with FastAPI, uvicorn, SQLAlchemy, and pytest
  - [x] Project structure includes app/, tests/, and .github/workflows/ directories
  - [x] .gitignore file is configured for Python projects
- **Files**: requirements.txt, .gitignore, app/__init__.py, tests/__init__.py
- **Status**: DONE

#### STORY-1.2: Database Models and Connection
- **Priority**: P0
- **Phase**: implement
- **Description**: Create SQLAlchemy models for Todo items and configure database connection
- **Acceptance Criteria**:
  - [x] Todo model has id (integer, primary key), title (string), description (string), completed (boolean)
  - [x] Database connection uses SQLite with SQLAlchemy
  - [x] Database tables are created on application startup
- **Files**: app/models.py, app/database.py
- **Status**: DONE

#### STORY-1.3: Pydantic Schemas
- **Priority**: P0
- **Phase**: implement
- **Description**: Create Pydantic schemas for request/response validation
- **Acceptance Criteria**:
  - [x] TodoCreate schema for creating todos (title, description, completed optional)
  - [x] TodoUpdate schema for updating todos (all fields optional)
  - [x] TodoResponse schema for API responses (includes id)
  - [x] Schemas include proper validation and documentation
- **Files**: app/schemas.py
- **Status**: DONE

#### STORY-1.4: CRUD Operations
- **Priority**: P0
- **Phase**: implement
- **Description**: Implement CRUD operations for Todo items
- **Acceptance Criteria**:
  - [x] create_todo function creates a new todo item
  - [x] get_todo function retrieves a single todo by ID
  - [x] get_todos function retrieves all todo items with optional pagination
  - [x] update_todo function updates an existing todo by ID
  - [x] delete_todo function deletes a todo by ID
  - [x] All operations return appropriate data or raise HTTPException for not found
- **Files**: app/crud.py
- **Status**: DONE

#### STORY-1.5: API Routes
- **Priority**: P0
- **Phase**: implement
- **Description**: Create FastAPI routes for all CRUD operations
- **Acceptance Criteria**:
  - [x] POST /todos - Create a new todo, returns 201 with created todo
  - [x] GET /todos - List all todos, returns 200 with array of todos
  - [x] GET /todos/{todo_id} - Get a specific todo, returns 200 or 404
  - [x] PUT /todos/{todo_id} - Update a todo, returns 200 or 404
  - [x] DELETE /todos/{todo_id} - Delete a todo, returns 204 or 404
  - [x] OpenAPI documentation is auto-generated and accessible at /docs
- **Files**: app/main.py, app/routes.py
- **Status**: DONE

### EPIC-2: Testing

#### STORY-2.1: Test Configuration and Fixtures
- **Priority**: P0
- **Phase**: test_auto
- **Description**: Set up pytest configuration and create test fixtures
- **Acceptance Criteria**:
  - [x] pytest.ini or pyproject.toml configured for pytest
  - [x] conftest.py contains fixtures for test database
  - [x] Test database is isolated from production database
  - [x] Fixtures provide clean database state for each test
- **Files**: pytest.ini, tests/conftest.py
- **Status**: DONE

#### STORY-2.2: CRUD Unit Tests
- **Priority**: P0
- **Phase**: test_auto
- **Description**: Write unit tests for CRUD operations
- **Acceptance Criteria**:
  - [x] Test create_todo creates a todo with valid data
  - [x] Test get_todo retrieves existing todo
  - [x] Test get_todo raises error for non-existent todo
  - [x] Test get_todos returns all todos
  - [x] Test update_todo modifies existing todo
  - [x] Test update_todo raises error for non-existent todo
  - [x] Test delete_todo removes existing todo
  - [x] Test delete_todo raises error for non-existent todo
- **Files**: tests/test_crud.py
- **Status**: DONE

#### STORY-2.3: API Endpoint Tests
- **Priority**: P0
- **Phase**: test_auto
- **Description**: Write integration tests for all API endpoints
- **Acceptance Criteria**:
  - [x] Test POST /todos returns 201 and created todo
  - [x] Test POST /todos returns 422 for invalid data
  - [x] Test GET /todos returns 200 with todo list
  - [x] Test GET /todos/{id} returns 200 for existing todo
  - [x] Test GET /todos/{id} returns 404 for non-existent todo
  - [x] Test PUT /todos/{id} returns 200 and updated todo
  - [x] Test PUT /todos/{id} returns 404 for non-existent todo
  - [x] Test DELETE /todos/{id} returns 204 for successful deletion
  - [x] Test DELETE /todos/{id} returns 404 for non-existent todo
- **Files**: tests/test_api.py
- **Status**: DONE

#### STORY-2.4: Test Coverage Verification
- **Priority**: P1
- **Phase**: test_auto
- **Description**: Ensure test coverage is at least 90%
- **Acceptance Criteria**:
  - [x] pytest-cov is configured
  - [x] Running tests with coverage shows >= 90% coverage
  - [x] Coverage report is generated and visible
- **Files**: pytest.ini (updated with coverage config)
- **Status**: DONE

### EPIC-3: CI/CD Pipeline

#### STORY-3.1: Docker Configuration
- **Priority**: P1
- **Phase**: cicd
- **Description**: Create Dockerfile for containerizing the application
- **Acceptance Criteria**:
  - [x] Dockerfile builds successfully
  - [x] Docker image runs the FastAPI application
  - [x] Application is accessible on port 8000
  - [x] Dockerfile follows best practices (multi-stage build, non-root user)
- **Files**: Dockerfile
- **Status**: DONE

#### STORY-3.2: GitHub Actions CI Pipeline
- **Priority**: P0
- **Phase**: cicd
- **Description**: Create GitHub Actions workflow for CI
- **Acceptance Criteria**:
  - [x] Workflow runs on push to main and pull requests
  - [x] Workflow installs dependencies
  - [x] Workflow runs all tests with coverage
  - [x] Workflow fails if tests fail or coverage is below 90%
  - [x] Workflow builds Docker image successfully
- **Files**: .github/workflows/ci.yml
- **Status**: DONE

### EPIC-4: Documentation

#### STORY-4.1: README Documentation
- **Priority**: P1
- **Phase**: validate
- **Description**: Create comprehensive README with setup and usage instructions
- **Acceptance Criteria**:
  - [x] README includes project description
  - [x] README includes installation instructions
  - [x] README includes API endpoint documentation
  - [x] README includes example requests/responses
  - [x] README includes Docker usage instructions
  - [x] README includes testing instructions
- **Files**: README.md
- **Status**: DONE

## Non-Functional Requirements
- [x] All tests pass
- [x] Docker build succeeds
- [x] CI pipeline is green
- [x] No hardcoded secrets or credentials
- [x] Error handling covers edge cases
- [x] README is accurate and complete
- [x] Test coverage >= 90% (96.73%)
- [x] OpenAPI documentation is available at /docs

## Manual Testing Results
All acceptance criteria have been manually verified:

### API Endpoints Tested
- [x] GET / - Returns API info with name, version, and docs link
- [x] GET /health - Returns {"status": "healthy"}
- [x] POST /todos - Creates todo, returns 201 with created todo
- [x] POST /todos with minimal data - Works with just title
- [x] POST /todos with completed=true - Creates completed todo
- [x] POST /todos without title - Returns 422 validation error
- [x] POST /todos with invalid title type - Returns 422 validation error
- [x] POST /todos with empty title - Returns 422 validation error
- [x] GET /todos - Returns list of todos with pagination info
- [x] GET /todos?completed=true - Filters by completed status
- [x] GET /todos/{id} - Returns specific todo
- [x] GET /todos/{id} for non-existent - Returns 404
- [x] PUT /todos/{id} - Updates todo, returns 200
- [x] PUT /todos/{id} partial update - Works with partial fields
- [x] PUT /todos/{id} for non-existent - Returns 404
- [x] DELETE /todos/{id} - Deletes todo, returns 204
- [x] DELETE /todos/{id} for non-existent - Returns 404
- [x] GET /docs - Returns 200 (OpenAPI docs accessible)

### Edge Cases Tested
- [x] Invalid data types are rejected with 422
- [x] Empty strings are rejected with 422
- [x] Non-existent resources return 404
- [x] Pagination works correctly
- [x] Filtering by completed status works