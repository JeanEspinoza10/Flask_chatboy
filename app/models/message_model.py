from app.models.base import BaseModel
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, Date,BigInteger
from sqlalchemy.orm import relationship

class Message(BaseModel):
    __tablename__ = "message"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(120))
    text = Column(String(255))
    # # Relacion con la tabla conversation
    conversation_id = Column(Integer, ForeignKey('conversations.id'))
    conversationrel = relationship("Conversation", uselist=False, back_populates="messen")

    # La fecha se grabar en año, mes, dia, hora, minutos, segundo y milisegundos
    fecha =Column(String(255))
    





