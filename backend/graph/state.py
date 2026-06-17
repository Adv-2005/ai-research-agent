from typing import TypedDict

class ResearchState(TypedDict, total=False):
    query: str

    tasks: dict

    web_report:str
    financial_report:str
    product_report:str

    critique_decision:str
    critique_feedback:str

    retry_count:int
    
    final_report:str


    
