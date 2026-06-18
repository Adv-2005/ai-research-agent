from langchain_qdrant import QdrantVectorStore

from qdrant_client import QdrantClient

from ingestion.embeddings import (
    get_embeddings
)

COLLECTION_NAME = "research_docs"


def create_vectorstore():

    client = QdrantClient(
        url="http://localhost:6333"
    )

    embeddings = get_embeddings()

    vectorstore = QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME,
        embedding=embeddings
    )

    return vectorstore

def ingest_chunks(chunks):

    embeddings = get_embeddings()

    QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        url="http://localhost:6333",
        collection_name=COLLECTION_NAME
    )

    print(
        f"Ingested {len(chunks)} chunks"
    )