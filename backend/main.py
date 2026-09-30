import os

from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl

from workflow.seo_graph import run_seo_workflow


app = FastAPI(
    title="Aurify Multi-Agent SEO Team",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SEORequest(BaseModel):

    website: HttpUrl
    goal: str = "Increase organic traffic"


@app.get("/")
def root():

    return {
        "message": "Aurify Multi-Agent SEO Team API",
        "status": "running"
    }


@app.post("/api/seo/analyze")
def analyze_seo(request: SEORequest):

    try:

        result = run_seo_workflow(
            str(request.website),
            request.goal
        )

        return result

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )