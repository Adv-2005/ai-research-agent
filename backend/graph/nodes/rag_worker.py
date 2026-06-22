from graph.state import ResearchState

from rag.hybrid_retriever import (
    get_hybrid_retriever
)

from rag.reranker import (
    rerank_documents
)

from prompts.rag_prompt import (
    RAG_PROMPT
)

from services.llms import llm

import logging

logger = logging.getLogger(__name__)


def rag_worker(
    state: ResearchState
) -> ResearchState:

    logger.info("RAG START")

    query = state["tasks"]["rag"]

    try:

        # ----------------------------
        # Hybrid Retrieval
        # ----------------------------

        retriever = get_hybrid_retriever()

        retrieved_docs = retriever.invoke(
            query
        )

        logger.info(
            f"Retrieved {len(retrieved_docs)} docs"
        )

        # ----------------------------
        # Reranking
        # ----------------------------

        reranked_docs = rerank_documents(
            query=query,
            documents=retrieved_docs,
            top_k=5
        )

        logger.info(
            f"Reranked to {len(reranked_docs)} docs"
        )

        # ----------------------------
        # Build Context
        # ----------------------------

        context = "\n\n".join(
            doc.page_content
            for doc in reranked_docs
        )

        # ----------------------------
        # Source Tracking
        # ----------------------------

        sources = []

        for doc in reranked_docs:

            sources.append({
                "source":
                    doc.metadata.get(
                        "source",
                        "unknown"
                    ),

                "page":
                    doc.metadata.get(
                        "page",
                        "unknown"
                    )
            })

        # ----------------------------
        # LLM Call
        # ----------------------------

        prompt = RAG_PROMPT.format(
            query=query,
            context=context
        )

        response = llm.invoke(
            prompt
        )

        logger.info("RAG COMPLETE")

        return {
            "rag_report":
                response.content,

            "rag_sources":
                sources
        }

    except Exception as e:

        logger.exception(
            "RAG WORKER FAILED"
        )

        return {
            "rag_report":
                f"RAG retrieval failed: {str(e)}",

            "rag_sources":
                []
        }