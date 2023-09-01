import logging
import os

import sentry_sdk
from dotenv import load_dotenv
from fastapi import FastAPI
from sentry_sdk.integrations.logging import LoggingIntegration
from sqladmin import Admin
from starlette.middleware.cors import CORSMiddleware

from app.admin.admin_config import configure_admin
from app.config import settings
from app.config.database import engine
from app.config.router_config import configure_routes
from app.routers.qr_tease import router_system as qr_route

load_dotenv()
log_integration = LoggingIntegration(level=logging.INFO, event_level=logging.ERROR)

sentry_sdk.init(dsn=os.getenv("SENTRY_LINK"), traces_sample_rate=1.0, integrations=[log_integration])


def create_app():
    """
    Создаем приложение"""
    app = FastAPI(
        title=settings.APP_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )
    # Включаем CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    configure_routes(app)
    configure_admin(app, engine)
    return app


app = create_app()
qr_app = FastAPI()
qr_app.include_router(qr_route)