from graph.state import ResearchState
from tools import (
    get_company_financials, resolve_ticker
)
from services.llms import llm
from prompts.financial_prompt import FINANCIAL_PROMPT
import logging

logger = logging.getLogger(__name__)


def structured_data_worker(
    state: ResearchState
):

    query = state["tasks"]["financial"]

    logger.info(
        "STRUCTURED DATA START"
    )

    ticker = resolve_ticker(query) 

    try:

        financial_data = (
            get_company_financials(ticker)
        )

    except Exception as e:

        logger.exception(e)

        return {
            "financial_report":
            f"Financial data unavailable: {e}"
        }

    prompt = FINANCIAL_PROMPT.format(
        financial_data=financial_data
    )

    response = llm.invoke(prompt)

    logger.info(
        "STRUCTURED DATA COMPLETE"
    )

    return {
        "financial_report":
        response.content
    }