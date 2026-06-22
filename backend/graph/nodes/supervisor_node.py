from prompts.report_prompt import REPORT_PROMPT
from ..state import ResearchState
from tools import search_tool
from services.llms import llm
import logging
logger = logging.getLogger(__name__)


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

