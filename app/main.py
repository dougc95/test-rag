# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Optional
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="RAG API Template",
    description="Simple FastAPI template for RAG project",
    version="0.1.0"
)

# Pydantic models
class QueryRequest(BaseModel):
    query: str
    top_k: Optional[int] = 3

class QueryResponse(BaseModel):
    answer: str
    sources: List[str] = []

# Routes
@app.get("/")
async def root():
    return {"message": "RAG API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    # This is a placeholder that will be replaced with actual RAG implementation
    return QueryResponse(
        answer=f"This is a mock response for: {request.query}",
        sources=["mock_source_1", "mock_source_2"]
    )

# Document endpoints
@app.post("/documents")
async def add_document(file_path: str, document_type: str = "text"):
    # Placeholder for document processing logic
    return {
        "status": "success",
        "message": f"Document {file_path} of type {document_type} would be processed here"
    }

@app.get("/documents")
async def list_documents():
    # Placeholder for listing documents
    return {
        "documents": [
            {"id": "doc1", "name": "Sample Document 1"},
            {"id": "doc2", "name": "Sample Document 2"}
        ]
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)