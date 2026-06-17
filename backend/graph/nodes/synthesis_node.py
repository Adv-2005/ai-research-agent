from graph.state import ResearchState

def synthesis_node(state: ResearchState) -> ResearchState:

    report = f"""
# Research Report

{state['web_report']}

---

{state['financial_report']}

---

{state['product_report']}
"""

    return {
        "final_report": report
    }