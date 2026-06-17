from prompts.critique_prompt import CRITIQUE_PROMPT
from graph.state import ResearchState
from services.llms import llm
import logging

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

    decision = response.content
    print("CRITIQUE EXECUTED")
    logger.info("CRITIQUE END")

    if "RETRY" in decision.upper():
        return {
            "critique_decision": "retry",
            "critique_feedback": decision
        }

    return {
        "critique_decision": "approve",
        "critique_feedback": decision
    }