from typing import TypedDict

class ResearchState(TypedDict, total=False):
    query: str
    search_results: str
    tasks: dict
    web_report:str
    financial_report:str
    product_report:str
    final_report:str


    
