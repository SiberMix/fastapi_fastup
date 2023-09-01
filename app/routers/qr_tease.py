import json
import os
import requests
from base64 import b64decode

import sentry_sdk
from fastapi import APIRouter, Depends
from starlette.requests import Request
from app.config.settings import qr_link_1c
from app.service.telegram_sender import TelegramBot

router_system = APIRouter()
telegram_bot = TelegramBot(os.getenv("BOT_TOKEN"))

class OneCResponseCode:
    SUCCESS = 201
    CONNECTION_ERROR = 418
    OTHER_ERROR = 500

def parse_message(body):
    return json.loads(body).get('qrcId'), round(json.loads(body).get('amount') / 100, 2)

def make_message(body, status):
    status_icons = {'success': '✅', 'error': '❌'}
    status_messages = {
        OneCResponseCode.SUCCESS: 'Обработан callback',
        OneCResponseCode.CONNECTION_ERROR: 'Не удалось установить соединение с 1С',
        OneCResponseCode.OTHER_ERROR: 'Необработан callback'
    }
    operation_icon = status_icons.get('success') if status == OneCResponseCode.SUCCESS else status_icons.get('error')
    operation_status = status_messages.get(status, 'Необработан callback')

    operation_id, operation_amount = parse_message(body)
    friendly_message = f'{operation_icon}[{status}] {operation_status}: {operation_id}, на сумму {operation_amount}'
    return friendly_message

def one_c_redirect(message: str) -> int:
    try:
        r = requests.post(url=qr_link_1c, json=json.loads(message))
        msg = make_message(message, r.status_code)
        with sentry_sdk.configure_scope() as scope:
            scope.set_context("Info", {'details': f'"{msg.split(": ")[1]}"'})
        sentry_sdk.capture_message(msg.split(': ')[0][1:])

        telegram_bot.send_message(os.getenv("CHAT_ID"), msg)
        return OneCResponseCode.SUCCESS
    except requests.ConnectionError as e:
        telegram_bot.send_message(os.getenv("CHAT_ID"), str(e))
        return OneCResponseCode.CONNECTION_ERROR

def take_message(data: bytes) -> str:
    base64_bytes = data.split(b'.')[1]
    base64_bytes += b'=' * (-len(base64_bytes) % 4)
    message_bytes = b64decode(base64_bytes, b'-_')
    message = message_bytes.decode('utf-8')
    return message

async def get_body(request: Request):
    result = await request.body()
    return result

@router_system.post('/')
def post_info(body: bytes = Depends(get_body)):
    """
    Отправить ответ на 1с и получить итог
    :return:
    """
    message = take_message(body)
    result = one_c_redirect(message)
    return result
