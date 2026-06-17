from graph.state import ResearchState

def critique_router(
    state: ResearchState
):

    if (
        state["critique_decision"] == "retry"
        and state["retry_count"] < 1
    ):
        return "retry"

    return "approve"