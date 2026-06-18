from graph.state import ResearchState
import logging

logger = logging.getLogger(__name__)

def increment_retry_node(
    state: ResearchState
) -> ResearchState:
    
    new_count = state["retry_count"] + 1

    logger.info(
        f"RETRY COUNT -> {new_count}"
    )

    return {
        "retry_count":
            new_count
    }