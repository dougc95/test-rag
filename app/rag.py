from langchain_community.document_loaders import PDFPlumberLoader
# Load a PDF document using PDFPlumberLoader
# Make sure to install the required package: pip install langchain-community[pdf]
# Adjust the path to your PDF file as necessary
import os
PATH = "./app/reforma.pdf"
if not os.path.exists(PATH):
    raise FileNotFoundError("The specified PDF file does not exist.")
loader = PDFPlumberLoader(PATH)
docs = loader.load()

print(f"Loaded {len(docs)} documents from PDF.")

print("First document content:")
print(docs[6].page_content[:500])  # Print the first 500 characters of the first document
print("Metadata of the first document:")
print(docs[6].metadata)  # Print metadata of the first document