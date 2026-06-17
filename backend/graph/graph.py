
import os

from .state import ResearchState
from .nodes.web_worker import web_worker
from .nodes.synthesis_node import synthesis_node
from .nodes.supervisor_node import supervisor_node
from .nodes.financial_worker import financial_worker
from .nodes.product_worker import product_worker
from langgraph.graph import StateGraph

builder = StateGraph(ResearchState)

builder.add_node("supervisor", supervisor_node)
builder.add_node("web_worker", web_worker)
builder.add_node("synthesis", synthesis_node)
builder.add_node("financial_worker", financial_worker)
builder.add_node("product_worker", product_worker)

builder.set_entry_point("supervisor")
builder.add_edge("supervisor", "web_worker")
builder.add_edge("supervisor", "financial_worker")
builder.add_edge("supervisor", "product_worker")
builder.add_edge("web_worker", "synthesis")
builder.add_edge("financial_worker", "synthesis")
builder.add_edge("product_worker", "synthesis")
builder.set_finish_point("synthesis")
graph = builder.compile()