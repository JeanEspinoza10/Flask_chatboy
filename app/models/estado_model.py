from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

# Estado trabajamos con:Finalizado, En proceso, Cerrado

class Estado(BaseModel):
    __tablename__ = "estatus"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80))
    status = Column(Boolean, default=True)
