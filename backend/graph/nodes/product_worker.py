from graph.state import ResearchState
from prompts.product_prompt import PRODUCT_PROMPT
from services.llms import llm
from tools import search_tool

def product_worker(
    state: ResearchState
) -> ResearchState:

    query = state["tasks"]["product"]

    search_results = search_tool.invoke(
        f"{query} products technology AI platform innovation"
    )

    prompt = PRODUCT_PROMPT.format(
        query=query,
        search_results=search_results
    )

    response = llm.invoke(prompt)

    return {
        "product_report": response.content
    }