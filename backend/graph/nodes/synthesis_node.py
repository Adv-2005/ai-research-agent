from graph.state import ResearchState
import logging

logger = logging.getLogger(__name__)

def synthesis_node(state: ResearchState) -> ResearchState:
    logger.info("SYNTHESIS START")

    report = f"""
# Research Report

{state['web_report']}

---

{state['financial_report']}

---

{state['product_report']}

---

{state['rag_report']}
"""

    return {
        "final_report": report
    }