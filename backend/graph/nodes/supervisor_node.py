from prompts.report_prompt import REPORT_PROMPT
from ..state import ResearchState
from tools import search_tool
from services.llms import llm
import logging
logger = logging.getLogger(__name__)


# def research_node(state: ResearchState) -> ResearchState:
#     query = state["query"]
#     logger.info(
#         f"Starting research for: {query}"
#     )
#     logger.info("Calling Tavily")
    
#     search_results = search_tool.invoke(query)
#     logger.info("Tavily completed")

    
#     prompt = REPORT_PROMPT.format(
#         query=query,
#         search_results=search_results
#     )
#     logger.info("Calling Ollama")
#     response = llm.invoke(prompt)
#     logger.info("Ollama completed")
    
#     return {"query": query, "report": response.content}

def supervisor_node(state: ResearchState) -> ResearchState:
    # Placeholder for supervisor logic
    query = state["query"]
    return{
        "tasks":{
            "web": query,
            "financial": query,
            "product": query
        }
    }

# def web_worker(state: ResearchState) -> ResearchState:
#     # Placeholder for web worker logic
#     query = state["tasks"]["web"]
#     results = search_tool.invoke(f"{query} latest news")

#     response = llm.invoke(WEB_PROMPT.format(results=results))
#     return {"web_report": response.content}