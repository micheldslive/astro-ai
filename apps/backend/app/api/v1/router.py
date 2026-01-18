from fastapi import APIRouter

from app.api.v1.agents.router import router as agents_router

routers = [agents_router]
v1_router = APIRouter(prefix="/v1")

for router in routers:
    v1_router.include_router(router)
