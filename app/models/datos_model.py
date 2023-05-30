from app.models.base import BaseModel
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Datos(BaseModel):
    __tablename__ ="usuarios"
    id =Column(Integer, primary_key=True, autoincrement=True)
    ws_id = Column(Integer, unique=True)
    state = Column(String(120))
    name = Column(String(120))
    phone = Column(String(120), unique=True)
    correo = Column(String(120))
    oficina = Column(String(120))