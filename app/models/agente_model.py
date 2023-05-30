from app.models.base import BaseModel
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from bcrypt import hashpw, gensalt, checkpw

class Agentes(BaseModel):
    __tablename__ ="agentes"
    id =Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120))
    correo = Column(String(120))
    password = Column(String(120), nullable=False)
    status = Column(Boolean, default=True)

    # Relacion con el rol
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship("RoleModel", back_populates='users')
    
    def hashPassword(self):
        pwd_encode = self.password.encode('utf-8')
        pwd_hash = hashpw(pwd_encode, gensalt(rounds=10))
        self.password = pwd_hash.decode('utf-8')

    def checkPassword(self, password):
        return checkpw(
            password.encode('utf-8'),
            self.password.encode('utf-8')
        )


