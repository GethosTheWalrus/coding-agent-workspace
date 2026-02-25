# Dockerfile for FastAPI Todo API
# Multi-stage build with non-root user and minimal layers

# ---------- Builder Stage ----------
FROM python:3.12-slim AS builder

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*

# Create a non-root user and group
RUN groupadd -r appgroup && useradd -r -g appgroup -d /src appuser

# Set working directory for building
WORKDIR /src

# Install Python dependencies (cached layer)
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application source code (the package)
COPY app/ ./app/
# Copy tests (only for CI) into a top‑level directory
COPY tests/ ./tests/
# Ensure no compiled bytecode remains in the tests directory
RUN find ./tests -type d -name "__pycache__" -exec rm -rf {} +

# Change ownership to non‑root user
RUN chown -R appuser:appgroup /src

# ---------- Runtime Stage ----------
FROM python:3.12-slim

# Create same non‑root user/group in runtime image
RUN groupadd -r appgroup && useradd -r -g appgroup -d /app appuser

WORKDIR /app

# Copy installed packages and scripts from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
# Copy application code (the package) directly into /app
COPY --from=builder /src/app ./
# Copy tests for CI (optional, not needed at runtime)
COPY --from=builder /src/tests ./tests

# Ensure non‑root ownership
RUN chown -R appuser:appgroup /app

# Switch to non‑root user
USER appuser

# Expose port for FastAPI (default 8000)
EXPOSE 8000

# Command to run the app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
