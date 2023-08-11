from app.service.service import Callback
from app.tasks.celery_config import tisa_celery

callback_api = Callback()

@tisa_celery.task
def send_email_callback(send_to, ticket):
    """
    Кидаем задачу в Celery на отправку письма всем пользователям из БД
    :return:
    """

    callback_api.send_to_email(to_send=send_to, ticket=ticket)
    return send_to

@tisa_celery.task
def send_email_user(send_to):
    """
    Отправляем клиенту сообщение что мы получили обратный звонок
    """
    callback_api.send_info_client(send_to)