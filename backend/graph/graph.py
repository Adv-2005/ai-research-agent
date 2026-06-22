
import os

from .state import ResearchState
from .nodes.web_worker import web_worker
from .nodes.synthesis_node import synthesis_node
from .nodes.supervisor_node import supervisor_node
from .nodes.structured_data_worker import structured_data_worker
from .nodes.product_worker import product_worker
from .nodes.critique_node import critique_node
from .nodes.conditional_router import critique_router
from .nodes.increment_retry_node import increment_retry_node
from .nodes.conditional_router import retry_router
from langgraph.graph import StateGraph
from .nodes.rag_worker import rag_worker

builder = StateGraph(ResearchState)

builder.add_node("supervisor", supervisor_node)
builder.add_node("web_worker", web_worker)
builder.add_node("synthesis", synthesis_node)
builder.add_node("financial_worker", structured_data_worker)
builder.add_node("product_worker", product_worker)
builder.add_node("critique", critique_node)
builder.add_node("increment_retry", increment_retry_node)
builder.add_node(
    "rag_worker",
    rag_worker
)


builder.set_entry_point("supervisor")
builder.add_edge("supervisor", "web_worker")
builder.add_edge("supervisor", "financial_worker")
builder.add_edge("supervisor", "product_worker")
builder.add_edge(
    "supervisor",
    "rag_worker"
)


builder.add_edge("web_worker", "critique")
builder.add_edge("financial_worker", "critique")
builder.add_edge("product_worker", "critique")
builder.add_edge(
    "rag_worker",
    "critique"
)
builder.add_conditional_edges(
    "critique",
    critique_router,
    {
        "retry_web": "increment_retry",
        "retry_financial": "increment_retry",
        "retry_product": "increment_retry",
        "retry_rag": "increment_retry",
        "approve": "synthesis"
    }
)
builder.add_conditional_edges(
    "increment_retry",
    retry_router,
    {
        "web_worker": "web_worker",
        "financial_worker": "financial_worker",
        "product_worker": "product_worker",
        "rag_worker": "rag_worker"  
    }
)
builder.set_finish_point("synthesis")
graph = builder.compile()