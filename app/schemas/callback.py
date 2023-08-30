from pydantic import BaseModel, EmailStr


class BodyCallback(BaseModel):
    name: str
    phone: str
    email: EmailStr
    city_from: str = ''
    city_to: str = ''
    weight: float
    volume: float
    place: int
