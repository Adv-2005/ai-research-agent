from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
import yfinance as yf 

load_dotenv()
COMPANIES = {
    "nvidia": "NVDA",
    "microsoft": "MSFT",
    "apple": "AAPL",
    "tesla": "TSLA",
    "amazon": "AMZN",
}

search_tool = TavilySearchResults(max_results=5)

def get_company_financials(ticker: str):

     

    stock = yf.Ticker(ticker)
    info = stock.info
    if not info:

        raise ValueError(
            f"No financial data found for {ticker}"
        )

    return {
        "name": info.get("longName"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "market_cap": info.get("marketCap"),
        "current_price": info.get("currentPrice"),
        "pe_ratio": info.get("trailingPE"),
        "profit_margin": info.get("profitMargins"),
        "revenue": info.get("totalRevenue"),
    }


def resolve_ticker(query):

    return COMPANIES.get(
        query.lower(),
        query
    )