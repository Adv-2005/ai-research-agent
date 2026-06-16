from prompts.report_prompt import REPORT_PROMPT
from .state import ResearchState
from tools import search_tool
from services.llms import llm
import logging
logger = logging.getLogger(__name__)


def research_node(state: ResearchState) -> ResearchState:
    query = state["query"]
    logger.info(
        f"Starting research for: {query}"
    )
    logger.info("Calling Tavily")
    
    search_results = search_tool.invoke(query)
    logger.info("Tavily completed")

    
    prompt = REPORT_PROMPT.format(
        query=query,
        search_results=search_results
    )
    logger.info("Calling Ollama")
    response = llm.invoke(prompt)
    logger.info("Ollama completed")
    
    return {"query": query, "report": response.content}