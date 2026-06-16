
import os

from .state import ResearchState
from .nodes import research_node
from langgraph.graph import StateGraph

builder = StateGraph(ResearchState)

builder.add_node("research", research_node)

builder.set_entry_point("research")
builder.set_finish_point("research")
graph = builder.compile()

def run_research(query: str):

    result = graph.invoke(
        {"query": query}
    )

    return result["report"]