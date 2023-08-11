from fastapi import APIRouter, FastAPI

from app.routers.callback import router_callback
from app.routers.system import router_system


def configure_routes(app: FastAPI):
    app.include_router(router_system, tags=["Системные"])
    app.include_router(router_callback, prefix="/api", tags=["Callback"])
