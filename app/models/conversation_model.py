from app.models.base import BaseModel
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, Date,BigInteger, Date
from sqlalchemy.orm import relationship

class Conversation(BaseModel):
    __tablename__="conversations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    agente_id = Column(Integer, ForeignKey("agentes.id"))
    usuario_id = Column(Integer, ForeignKey("personal.id"))
    estado_id = Column(Integer, ForeignKey("estatus.id"))

    fecha = Column(Date)
    messen = relationship("Message", uselist=True, back_populates='conversationrel')
    sendmess = relationship("SendMessage", uselist=True, back_populates='conversationrolsend')






