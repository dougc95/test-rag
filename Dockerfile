# Use the latest Python 3.10 image (compatible with LangChain 0.1.3)
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app/main.py

# Set work directory
WORKDIR /app

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    iputils-ping \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install LangChain version 0.1.3
RUN pip install langchain==0.1.3

RUN pip install -qU "langchain[langchain-ollama]"

RUN pip install uvicorn

RUN pip install fastapi

RUN pip install pgvector psycopg2-binary SQLAlchemy

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]  