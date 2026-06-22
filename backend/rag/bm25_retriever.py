from langchain_community.retrievers import BM25Retriever
from ingestion.document_store import (
    load_chunks
)


def get_bm25_retriever():

    chunks = load_chunks()

    retriever = (
        BM25Retriever.from_documents(
            chunks
        )
    )

    retriever.k = 10

    return retriever