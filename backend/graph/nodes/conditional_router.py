from graph.state import ResearchState

def critique_router(
    state: ResearchState
):

    if (
        state["critique_decision"] != "retry"
        or state["retry_count"] >= 1
    ):
        return "approve"

    worker = state.get("target_worker", "none")

    if worker == "web":
        return "retry_web"
    elif worker == "financial":
        return "retry_financial"
    elif worker == "product":
        return "retry_product"
    elif worker == "rag":
        return "retry_rag"
    
    return "approve"

def retry_router(state):

    worker = state["target_worker"]

    if worker == "web":
        return "web_worker"

    elif worker == "financial":
        return "financial_worker"

    elif worker == "product":
        return "product_worker"
    elif worker == "rag":
        return "rag_worker"

    return "web_worker"