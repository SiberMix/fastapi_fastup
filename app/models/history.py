from sqlalchemy import Column, Integer, String

from app.config.database import Base


class HistoryTicket(Base):
    """
    История заявок с тизы
    """

    __tablename__ = "history_ticket"

    id = Column(Integer, primary_key=True, index=True)
    send_to = Column(String, index=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)
    city_from = Column(String)
    city_to = Column(String)
    weight = Column(Integer)
    volume = Column(Integer)
    place = Column(String)
