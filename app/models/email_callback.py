from sqlalchemy import Column, Integer, String

from app.config.database import Base


class EmailModel(Base):
    """
    Почты куда будет отправлять письмо с просьбой обратного звонка
    """

    __tablename__ = "Callbacks"
    id = Column(Integer, primary_key=True)
    email_login = Column(String(255), nullable=False)
