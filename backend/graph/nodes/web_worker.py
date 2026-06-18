from prompts.web_prompt import WEB_PROMPT
from services.llms import llm
from tools import search_tool
from graph.state import ResearchState

import logging
logger = logging.getLogger(__name__)

def web_worker(state: ResearchState) -> ResearchState:
    query = state["tasks"]["web"]
    logger.info("web Start")

    logger.info(
        f"Web worker started for: {query}"
    )

    search_results = search_tool.invoke(
        f"{query} latest news developments"
    )

    logger.info(
        "Web search completed"
    )
    critique_feedback = state.get("critique_feedback", "")

    prompt = WEB_PROMPT.format(
        query=query,
        search_results=search_results,
        critique_feedback=critique_feedback
    )

    response = llm.invoke(prompt)

    logger.info(
        "Web worker completed"
    )
    logger.info(f"Web keys: {state.keys()}")
    
    return {
        "web_report": response.content
    }