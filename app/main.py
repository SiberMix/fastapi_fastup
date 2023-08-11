from fastapi import FastAPI
from sqladmin import Admin

from app.admin.admin_config import configure_admin
from app.config import settings
from app.config.database import engine
from app.config.router_config import configure_routes


def create_app():
    """
    Создаем приложение"""
    app = FastAPI(
        title=settings.APP_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )

    configure_routes(app)
    configure_admin(app, engine)
    return app


app = create_app()
