from fastapi import FastAPI

from app.routers.brands import router as brands_router
from app.routers.vehicles import router as vehicles_router

app = FastAPI(title="C2S Desafio Técnico", version="0.1.0")

app.include_router(brands_router, tags=["brands"])
app.include_router(vehicles_router, tags=["vehicles"])
