from graph.state import ResearchState

def increment_retry_node(
    state: ResearchState
) -> ResearchState:

    return {
        "retry_count":
            state["retry_count"] + 1
    }