from ingestion.loader import load_pdf
from ingestion.splitter import split_documents
from ingestion.qdrant_store import ingest_chunks
from rag.retriever import get_retriever


docs = load_pdf(
    "uploads/MML_Module1.pdf"
)

chunks = split_documents(
    docs
)

ingest_chunks(
    chunks
)

retriever = get_retriever()

results = retriever.invoke(
    "What is machine learning?"
)

print(results[0].page_content)