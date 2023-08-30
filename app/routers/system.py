from fastapi import APIRouter
import requests
# Определите основной API-роутер
from starlette.responses import RedirectResponse

from app.config.settings import link_lk_btk

router_system = APIRouter()


@router_system.get("/ping")
def ping():
    """
    Пингуем сайт - если ответ ок - значит работает
    """
    return {"status": "success"}


@router_system.get("/")
def redirect_redoc():
    return RedirectResponse(url="/redoc")

@router_system.get("/getCoords")
def get_coords():
    """
    Получить координаты
    :return:
    """
    url = link_lk_btk + "/v1/getTerminalCoords"
    result = requests.get(url).json()
    return result