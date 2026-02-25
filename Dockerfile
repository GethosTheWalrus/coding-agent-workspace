# Dockerfile for FastAPI Todo API
# Multi-stage build with non-root user and minimal layers

# ---------- Builder Stage ----------
FROM python:3.12-slim AS builder

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*

# Create a non-root user and group
RUN groupadd -r appgroup && useradd -r -g appgroup -d /app appuser

# Set working directory
WORKDIR /app

# Install Python dependencies (cached layer)
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY app/ ./app/
COPY .env .  # optional environment file

# Change ownership to non-root user
RUN chown -R appuser:appgroup /app

# ---------- Runtime Stage ----------
FROM python:3.12-slim

# Create same non-root user/group in runtime image
RUN groupadd -r appgroup && useradd -r -g appgroup -d /app appuser

WORKDIR /app

# Copy only the installed packages from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
# Copy application code
COPY --from=builder /app ./app
COPY --from=builder /app/.env .

# Ensure non-root ownership
RUN chown -R appuser:appgroup /app

# Switch to non-root user
USER appuser

# Expose port for FastAPI (default 8000)
EXPOSE 8000

# Command to run the app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
