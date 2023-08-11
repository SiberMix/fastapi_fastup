from sqladmin import ModelView
from app.models.email_callback import EmailModel


class EmailForSend(ModelView, model=EmailModel):
    """
    Список почт, куда отправлять обратный звонок
    """

    name = "Почта обратный звонок"
    name_plural = "Почты обратного звонка"
    icon = "fa-solid fa-envelope"
    column_list = [EmailModel.email_login]
