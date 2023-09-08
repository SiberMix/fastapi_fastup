import os

from dotenv import load_dotenv
from fastapi import APIRouter, Depends

# Определите основной API-роутер
from sentry_sdk import capture_message
from sqlalchemy.orm import Session

from app.config.database import get_db_session
from app.models import EmailModel, HistoryTicket
from app.schemas.callback import BodyCallback
from app.service.telegram_sender import TelegramBot
from app.tasks.tasks import send_email_callback, send_email_user

load_dotenv()
router_callback = APIRouter()


telegram_bot = TelegramBot(bot_token=os.getenv('BOT_TOKEN'))
@router_callback.post("/callback")
async def post_callback(ticket: BodyCallback, db: Session = Depends(get_db_session)):
    """
    Отправить обратный звонок
    """

    query = db.query(EmailModel).all()
    mission_list = []
    for item in query:
        send_email_callback.delay(
            send_to=item.email_login,
            name=ticket.name,
            phone=ticket.phone,
            email=ticket.email,
            city_from=ticket.city_from,
            city_to=ticket.city_to,
            weight=ticket.weight,
            volume=ticket.volume,
            place=ticket.place
        )

        mission_list.append(item.email_login)
    send_email_user.delay(send_to=ticket.email)
    message = f'Заявка с сайта: \n ' \
              f'Телефон: {ticket.phone} \n ' \
              f'Почта: {ticket.email} \n ' \
              f'Откуда: {ticket.city_from} \n ' \
              f'Куда: {ticket.city_to} \n ' \
              f'Вес: {ticket.weight} \n ' \
              f'Объем: {ticket.volume} \n ' \
              f'Имя: {ticket.name} \n ' \
              f'Мест: {ticket.place} \n '
    history_ticket = HistoryTicket(
        send_to=ticket.email,
        name=ticket.name,
        phone=ticket.phone,
        email=ticket.email,
        city_from=ticket.city_from,
        city_to=ticket.city_to,
        weight=ticket.weight,
        volume=ticket.volume,
        place=ticket.place
    )
    db.add(history_ticket)
    db.commit()
    telegram_bot.send_message(chat_id=os.getenv('CHAT_ID'), message=message)
    capture_message(message)

    return mission_list
