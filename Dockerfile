# Dockerfile for FastAPI Todo API
# Build stage
FROM python:3.12-slim AS builder

# Set working directory
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY app/ ./app/
COPY .env .  # optional environment file

# Runtime stage
FROM python:3.12-slim
WORKDIR /app

# Copy only the installed packages from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /app ./app
COPY requirements.txt .

# Expose port for FastAPI (default 8000)
EXPOSE 8000

# Command to run the app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
