from prompts.financial_prompt import FINANCIAL_PROMPT
from graph.state import ResearchState
from services.llms import llm
from tools import search_tool

def financial_worker(
    state: ResearchState
) -> ResearchState:

    query = state["tasks"]["financial"]

    search_results = search_tool.invoke(
        f"{query} earnings revenue profit growth"
    )

    prompt = FINANCIAL_PROMPT.format(
        query=query,
        search_results=search_results
    )

    response = llm.invoke(prompt)

    return {
        "financial_report": response.content
    }