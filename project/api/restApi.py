from pydantic import BaseModel
from fastapi import FastAPI

#from core.logging import LOGGER
#from project.utils import utility

app = FastAPI()
#logger = LOGGER.get_logger()


class JobDescription(BaseModel):
    job_description: str
    model: str


@app.get("/")
async def health_check():
    #logger.info("QnA Maker")
    return {"message": "Welcome to QnA Maker"}


@app.get("/predictQnA")
async def get_QnA(job_description: str, model: str):
    #logger.info("inside get_QnA")
    #return utility.retrieve_QnA_by_jd(job_description)
    return "test"
