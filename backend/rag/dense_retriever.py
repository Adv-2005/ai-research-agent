from langchain_qdrant import (
    QdrantVectorStore
)

from qdrant_client import (
    QdrantClient
)

from ingestion.embeddings import (
    get_embeddings
)

COLLECTION_NAME = "research_docs"


def get_dense_retriever():

    client = QdrantClient(
        url="http://localhost:6333"
    )

    vectorstore = QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME,
        embedding=get_embeddings()
    )

    return vectorstore.as_retriever(
        search_kwargs={
            "k": 10
        }
    )