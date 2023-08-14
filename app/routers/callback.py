from fastapi import APIRouter, Depends

# Определите основной API-роутер
from sqlalchemy.orm import Session

from app.config.database import get_db_session
from app.models import EmailModel
from app.schemas.callback import BodyCallback
from app.tasks.tasks import send_email_callback, send_email_user

router_callback = APIRouter()

@router_callback.post("/callback")
def post_callback(ticket: BodyCallback, db: Session = Depends(get_db_session)):
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
    return mission_list
