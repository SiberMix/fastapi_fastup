import json
from base64 import b64decode

import requests
from fastapi import APIRouter
from starlette.requests import Request

from app.config.settings import qr_link_1c

router_system = APIRouter()


def one_c_redirect(message: str) -> int:
    try:
        r = requests.post(url=qr_link_1c, json=json.loads(message))

        # Отправка в телегу об чеке
        if r.status_code in [201]:
            return 200
        return r.status_code
    except requests.ConnectionError:
        # Отправка в телегу об ошибке чека
        return 418


def take_message(data: bytes) -> str:
    base64_bytes = data.split(b'.')[1]
    base64_bytes += b'=' * (-len(base64_bytes) % 4)
    message_bytes = b64decode(base64_bytes, b'-_')
    message = message_bytes.decode('utf-8')
    return message


@router_system.post('/')
async def post_info(request: Request):
    """
    Отправить ответ на 1с и получить итог
    :return:
    """
    body = await request.body()
    message = take_message(body)

    result = one_c_redirect(message)
    return result
