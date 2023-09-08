from fastapi import APIRouter, FastAPI

from app.routers.callback import router_callback
from app.routers.system import router_system
from app.routers.logs import router as router_log


def configure_routes(app: FastAPI):
    app.include_router(router_system, tags=["Системные"])
    app.include_router(router_callback, prefix="/api", tags=["Callback"])
    app.include_router(router_log, tags=["LOGS"])
