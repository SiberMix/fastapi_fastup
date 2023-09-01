from fastapi import FastAPI
from sqladmin import Admin

from app.admin.models.callback import EmailForSend
from app.admin.models.history import HistorTicket
from app.admin.security_admin import authentication_backend


def configure_admin(app: FastAPI, engine: str):
    admin = Admin(
        app,
        engine,
        title="ТИЗА - АДМИНИСТРАТОР",
        authentication_backend=authentication_backend,
    )

    admin_views = [EmailForSend,
                   HistorTicket]

    for view in admin_views:
        admin.add_view(view)
