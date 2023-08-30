from app.service.service import Callback
from app.tasks.celery_config import tisa_celery

callback_api = Callback()

@tisa_celery.task
def send_email_callback(send_to, name, phone, email, city_from, city_to, weight, volume, place):
    """
    Кидаем задачу в Celery на отправку письма всем пользователям из БД
    :return:
    """
    callback_api.send_to_email(send_to, name, phone, email, city_from, city_to, weight, volume, place)

    return send_to
1
@tisa_celery.task
def send_email_user(send_to):
    """
    Отправляем клиенту сообщение что мы получили обратный звонок
    """
    callback_api.send_info_client(send_to)