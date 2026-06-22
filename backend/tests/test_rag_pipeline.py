from graph.state import ResearchState
from graph.nodes.rag_worker import rag_worker

state = {
    "tasks": {
        "rag": "What is gradient descent?"
    }
}

result = rag_worker(state)

print(result["rag_report"])
print(result["rag_sources"])