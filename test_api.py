import requests
import json

# Base URL of the API
BASE_URL = "http://localhost:8000"

def test_root():
    response = requests.get(f"{BASE_URL}/")
    print("Root endpoint:", response.json())

def test_health():
    response = requests.get(f"{BASE_URL}/health")
    print("Health endpoint:", response.json())

def test_query():
    payload = {
        "query": "What is RAG?",
        "top_k": 2
    }
    response = requests.post(f"{BASE_URL}/query", json=payload)
    print("Query endpoint:", response.json())

def test_documents_list():
    response = requests.get(f"{BASE_URL}/documents")
    print("Documents list endpoint:", response.json())

def test_document_add():
    params = {
        "file_path": "example.txt",
        "document_type": "text"
    }
    response = requests.post(f"{BASE_URL}/documents", params=params)
    print("Document add endpoint:", response.json())

if __name__ == "__main__":
    print("Testing the FastAPI endpoints...\n")
    test_root()
    test_health()
    test_query()
    test_documents_list()
    test_document_add()
    print("\nAll tests completed!")
