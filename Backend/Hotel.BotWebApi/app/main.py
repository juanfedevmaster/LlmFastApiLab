from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Hotel Bot Web API - Agente RAG")

app.include_router(router)