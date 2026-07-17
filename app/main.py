from fastapi import FastAPI

from app.api.v1.api import api_router

app = FastAPI(
    title="GenAI TalentHub API",
    description="AI-powered Resume Intelligence Platform",
    version="1.0.0",
)

app.include_router(api_router)