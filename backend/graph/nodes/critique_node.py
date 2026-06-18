from prompts.critique_prompt import CRITIQUE_PROMPT
from graph.state import ResearchState
from services.llms import llm
import logging
import re

logger = logging.getLogger(__name__)


def critique_node(
    state: ResearchState
) -> ResearchState:
    logger.info("CRITIQUE START")

    prompt = CRITIQUE_PROMPT.format(
        web_report=state["web_report"],
        financial_report=state["financial_report"],
        product_report=state["product_report"]
    )

    response = llm.invoke(prompt)

    content = response.content
    
    decision = "approve"
    target_worker = "none"

    upper_content = content.upper()

    if "DECISION: RETRY" in upper_content:
        decision = "retry"
    worker_match = re.search(r"WORKER:\s*(WEB|FINANCIAL|PRODUCT|NONE)", upper_content)
    if worker_match:
        target_worker = worker_match.group(1).lower()
    logger.info(f"Critique Decision: {decision}")
    logger.info(f"Critique Target Worker: {target_worker}")

    return{
        "critique_decision": decision,
        "target_worker": target_worker,
        "critique_feedback": content
    }