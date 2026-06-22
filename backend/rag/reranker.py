from sentence_transformers import (
    CrossEncoder
)

model = CrossEncoder(
    "BAAI/bge-reranker-base"
)


def rerank_documents(
    query: str,
    documents: list,
    top_k: int = 5
):

    pairs = [
        (
            query,
            doc.page_content
        )
        for doc in documents
    ]

    scores = model.predict(
        pairs
    )

    ranked = sorted(
        zip(documents, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        doc
        for doc, _
        in ranked[:top_k]
    ]