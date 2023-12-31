from sqladmin import ModelView

from app.models import HistoryTicket


class HistotyTicket(ModelView, model=HistoryTicket):
    """
    Список почт, куда отправлять обратный звонок
    """

    name = "Логи заявок"
    name_plural =  "Логи заявок"
    icon = "fa-solid fa-envelope"
    column_list = [HistoryTicket.email,
                   HistoryTicket.send_to,
                   HistoryTicket.name,
                   HistoryTicket.phone,
                   HistoryTicket.city_from,
                   HistoryTicket.city_to,
                   HistoryTicket.weight,
                   HistoryTicket.volume,
                   HistoryTicket.place]

