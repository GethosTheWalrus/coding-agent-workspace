"""FastAPI application entry point."""
from fastapi import FastAPI
from app.database import init_db
from app.routes import router

# Create FastAPI application
app = FastAPI(
    title="Todo API",
    description="A REST API for managing todo items",
    version="1.0.0"
)

# Include the todos router
app.include_router(router)


@app.on_event("startup")
def startup_event():
    """Initialize the database on application startup."""
    init_db()


@app.get("/")
def read_root():
    """Root endpoint returning API information."""
    return {
        "name": "Todo API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}