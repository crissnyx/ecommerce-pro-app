# Simple Dockerfile for Streamlit app (Python 3.10)
FROM python:3.10-slim

# Avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    STREAMLIT_SERVER_PORT=8501

WORKDIR /app

# Install system deps (keep minimal; add extras if you need them)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt /app/requirements.txt

# Install Python deps
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

# Copy app source
COPY . /app

# Create a non-root user and switch
RUN useradd --create-home appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8501

# Default command: run Streamlit app (adjust filename if different)
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.headless", "true", "--server.enableCORS", "false"]