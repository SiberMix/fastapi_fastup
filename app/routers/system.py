from fastapi import APIRouter

# Определите основной API-роутер
from starlette.responses import RedirectResponse

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
