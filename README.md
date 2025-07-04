# RAG API Project

This project implements a Retrieval-Augmented Generation (RAG) API using FastAPI and LangChain. The current implementation provides a basic API structure that will be integrated with RAG capabilities in future iterations.

## Project Structure

```
/test-rag/
├── app/
│   ├── __init__.py
│   └── main.py                  # FastAPI entry point
├── data/                       # Directory for storing documents and embeddings (to be created)
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── test_api.py                 # Script to test API endpoints
```

## Current Features

- Basic FastAPI application structure
- Placeholder endpoints for RAG functionality:
  - Root endpoint (`/`)
  - Health check endpoint (`/health`)
  - Query endpoint (`/query`) for RAG queries
  - Document management endpoints (`/documents`)
- Docker configuration for containerized deployment
- Test script for API validation

## Prerequisites

- Python 3.8+
- pip (Python package manager)

## Installation

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/test-rag.git
   cd test-rag
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Using Docker

1. Build and start the containers:
   ```bash
   docker-compose up --build
   ```

## Running the API

### Local Development

Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

The API will be available at http://127.0.0.1:8000

### Using Docker

```bash
docker-compose up
```

## Testing the API

1. With the API running, execute the test script:
   ```bash
   python test_api.py
   ```

2. Alternatively, access the interactive API documentation at http://127.0.0.1:8000/docs to test endpoints manually.

## API Endpoints

- `GET /`: Root endpoint, confirms API is running
- `GET /health`: Health check endpoint
- `POST /query`: Endpoint for RAG queries
  - Request body: `{"query": "your question here", "top_k": 3}`
  - Response: `{"answer": "response text", "sources": ["source1", "source2"]}`
- `GET /documents`: List available documents
- `POST /documents`: Add a new document
  - Parameters: `file_path` (string), `document_type` (string, default: "text")

## Next Steps

- Implement actual document processing logic
- Connect to a vector database (Chroma, FAISS, or Pinecone)
- Implement the RAG pipeline using LangChain
- Add authentication and security features
- Expand test coverage

## License

[Specify your license here]
