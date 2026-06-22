from ingestion.loader import load_pdf
from ingestion.splitter import split_documents
from ingestion.qdrant_store import ingest_chunks
from rag.hybrid_retriever import get_hybrid_retriever
from ingestion.document_store import save_chunks
from rag.reranker import (
    rerank_documents
)

docs = load_pdf(
    "uploads/MML_Module1.pdf"
)

chunks = split_documents(
    docs
)

save_chunks(chunks)

ingest_chunks(
    chunks
)

retriever = get_hybrid_retriever()
query = "What is Tom M Mitchell's definition of machine learning?"

docs = retriever.invoke(
    query
)
reranked = rerank_documents(
    query,
    documents=docs
)

print(len(docs))

for doc in docs:
    print(doc.page_content[:300])
# print(docs[0].metadata)
# print(docs[0].page_content[:300])


for doc in reranked:

    print("=" * 50)

    print(doc.page_content[:500])