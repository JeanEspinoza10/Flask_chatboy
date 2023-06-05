from app.models.base import BaseModel
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, Date,BigInteger
from sqlalchemy.orm import relationship

class SendMessage(BaseModel):
    __tablename__ ="send"

    id = Column(Integer,  primary_key=True, autoincrement=True)
    text = Column(String(255))
    # Relacion de muchos a uno con converstion
    conversation_id = Column(Integer, ForeignKey('conversations.id'))
    conversationrolsend = relationship("Conversation",  uselist=False, back_populates="sendmess")

    fecha =Column(String(255))

