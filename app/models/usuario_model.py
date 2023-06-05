from app.models.base import BaseModel
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship

class Usuarios(BaseModel):
    __tablename__ = "personal"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120))
    telephone = Column(String(120),  unique=True)
    oficina = Column(String(120),  unique=True)
    correo =  Column(String(120),  unique=True)
