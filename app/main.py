from fastapi import FastAPI, Depends, APIRouter
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from app.config import settings
from app.config.database import get_db_session

api = APIRouter()


@cbv(api)
class APIRoutes:
    db: Session = Depends(get_db_session)

    @api.get("/")
    def index(self):
        return {"success": True}


def create_app():
    app = FastAPI(
        title=settings.APP_NAME, 
        openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )
    @app.get('/')
    def start():
        return {'ok': True}
    app.include_router(api, prefix="/api")

    return app