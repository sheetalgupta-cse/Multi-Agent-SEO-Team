from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agents.manager import seo_manager


app = FastAPI(
    title="Aurify AI SEO Team API",
    version="1.0.0"
)


# --------------------------------
# CORS
# --------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
        "http://localhost:5174",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------
# Request Model
# --------------------------------

class SEORequest(BaseModel):
    website: str
    business_goal: str


# --------------------------------
# Health Check
# --------------------------------

@app.get("/")
def home():
    return {
        "status": "online",
        "service": "Aurify AI SEO Team"
    }


# --------------------------------
# SEO Analysis
# --------------------------------

@app.post("/api/analyze")
def analyze_seo(request: SEORequest):

    try:

        result = seo_manager(
            request.website,
            request.business_goal
        )

        return result

    except Exception as error:

        print("SEO ANALYSIS ERROR:", error)

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )