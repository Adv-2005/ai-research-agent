from langchain_classic.retrievers import (
    EnsembleRetriever
)

from rag.bm25_retriever import (
    get_bm25_retriever
)

from rag.dense_retriever import (
    get_dense_retriever
)


def get_hybrid_retriever():

    bm25 = get_bm25_retriever()

    dense = get_dense_retriever()

    hybrid = EnsembleRetriever(
        retrievers=[
            bm25,
            dense
        ],
        weights=[
            0.3,
            0.7
        ]
    )

    return hybrid