from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.config.database import get_db_session
from app.models import HistoryTicket

router = APIRouter()

# Получить максимальное количество мест (place) в заявках
@router.get("/api/max_places")
def max_places(db: Session = Depends(get_db_session)):
    """
    Получить максимальное количество мест (place) в заявках
    """
    max_place = db.query(HistoryTicket).with_entities(HistoryTicket.place).order_by(HistoryTicket.place.desc()).first()
    return {"max_places": max_place[0] if max_place else 0}

# Получить максимальный обьем (volume) в заявках
@router.get("/api/max_volume")
def max_volume(db: Session = Depends(get_db_session)):
    """
    Получить максимальный объем (volume) в заявках
    """
    max_volume = db.query(HistoryTicket).with_entities(HistoryTicket.volume).order_by(HistoryTicket.volume.desc()).first()
    return {"max_volume": max_volume[0] if max_volume else 0}

@router.get("/api/max_weight")
def max_weight(db: Session = Depends(get_db_session)):
    """
    Получить максимальный объем (volume) в заявках
    """
    max_weight = db.query(HistoryTicket).with_entities(HistoryTicket.weight).order_by(HistoryTicket.weight.desc()).first()
    return {"max_weight": max_weight[0] if max_weight else 0}

# Получить количество заявок из конкретного города
@router.get("/api/requests_from_city")
def requests_from_city(city: str, db: Session = Depends(get_db_session)):
    """
    Получить количество заявок из конкретного города
    """
    count = db.query(HistoryTicket).filter(HistoryTicket.city_from == city).count()
    return {"requests_from_city": count if count else 0}

# Получить количество заявок в конкретный город
@router.get("/api/requests_to_city")
def requests_to_city(city: str, db: Session = Depends(get_db_session)):
    """
    Получить количество заявок в конкретный город
    """
    count = db.query(HistoryTicket).filter(HistoryTicket.city_to == city).count()
    return {"requests_to_city": count if count else 0}

# Получить количество заявок между конкретными городами
@router.get("/api/requests_between_cities")
def requests_between_cities(city_from: str, city_to: str, db: Session = Depends(get_db_session)):
    """
    Получить количество заявок между конкретными городами
    """
    count = db.query(HistoryTicket).filter(HistoryTicket.city_from == city_from, HistoryTicket.city_to == city_to).count()
    return {"requests_between_cities": count if count else 0}
@router.get("/api/total_sum")
def total_sum(db: Session = Depends(get_db_session)):
    """
    Получить общую сумму заявок
    """
    total = db.query(func.count(HistoryTicket.id)).scalar()
    return {"total_sum": total if total else 0}
