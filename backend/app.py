from fastapi import FastAPI
from pydantic import BaseModel
import logging
from api.upload import router as upload_router


logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s - "
        "%(levelname)s - "
        "%(name)s - "
        "%(message)s"
    )
)
logger = logging.getLogger(__name__)


from graph.graph import graph
app = FastAPI()

app.include_router(upload_router)


class ResearchRequest(BaseModel):
    query: str
    type: str

@app.post("/research")
def research(request: ResearchRequest):
    logger.info(
        f"Received research request: {request.query}"
    )
    result = graph.invoke(
        {
            "query": request.query,
            "retry_count": 0
        }
    )
    print(result)
    logger.info("Graph execution completed")
    # Return an object with a `report` field so clients receive a JSON object
    return {"report": result["final_report"]}