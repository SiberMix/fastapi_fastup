import os

from celery import Celery
from dotenv import load_dotenv

load_dotenv()
tisa_celery = Celery()
tisa_celery.conf.broker_url = (
    f"redis://{os.getenv('REDIS_HOST')}:{os.getenv('REDIS_PORT')}/9"
)

tisa_celery.conf.broker_connection_retry_on_startup = True
tisa_celery.autodiscover_tasks(['app.tasks'])



class CeleryTaskQueue:
    def __init__(self, app):
        self.app = app

    def add_task(self, task_name, *args, **kwargs):
        task = self.app.send_task(task_name, args=args, kwargs=kwargs)
        return task


task_queue = CeleryTaskQueue(tisa_celery)
