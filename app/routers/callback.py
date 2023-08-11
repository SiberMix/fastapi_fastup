from fastapi import APIRouter, Depends

# Определите основной API-роутер
from sqlalchemy.orm import Session

from app.config.database import get_db_session
from app.models import EmailModel
from app.schemas.callback import BodyCallback
from app.service.service import Callback
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
        result = send_email_callback(send_to=item.email_login, ticket=ticket)
        mission_list.append(result)
    send_email_user(send_to=ticket.email)
    return mission_list
