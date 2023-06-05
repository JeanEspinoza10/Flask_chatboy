from app import db
from app.models.usuario_model import Usuarios
from app.models.conversation_model import Conversation
from app.models.estado_model import Estado
from app.models.message_model import Message
from app.utils.time import Fechas

tiempo = Fechas()

class Save:
    def __init__(self):
        self.usuarios = Usuarios
        self.conversation = Conversation
        self.estado = Estado
        self.mensajes = Message
    def personal(self, name, number):
        data={
                "name": name,
                "telephone":number
            }
        try:
            telephone = data["telephone"]
            review = self.usuarios.where(telephone=telephone).first()
            if not review:
                new_record = self.usuarios.create(**data)
                db.session.add(new_record)
                db.session.commit()            
        except Exception as e:
            db.session.rollback()
            print("Ocurrio un error", e)
    
    def message(self,text, tipo, number, time):
        # creando los datos para la tabla de mensajes

        data = {
            "tipo":tipo,
            "text":text,
            "fecha": tiempo.transtime(time)
        }
        
        try:
            # Buscando si tiene alguna conversacion activa el numero
            usuario = self.usuarios.where(telephone=number).first()
            estatus = self.estado.where(name="En proceso").first()
            convertasion_activate = self.conversation.where(usuario_id =usuario.id).filter_by(estado_id=estatus.id).first()
    
            # Creando conversacion si es que no existe
            if not convertasion_activate:
                data_conversation={
                    "usuario_id":usuario.id,
                    "estado_id": estatus.id,
                    "fecha": tiempo.fecha()
                }
                new_record= self.conversation.create(**data_conversation)
                db.session.add(new_record)
                db.session.commit()
            
            convertasion_activate = self.conversation.where(usuario_id=usuario.id).filter_by(estado_id=estatus.id).first()
            
            
            # Creando en la tabla message
            data["conversation_id"] = convertasion_activate.id
            new_record = self.mensajes.create(**data)
            db.session.add(new_record)
            db.session.commit()


        except Exception as e:
            db.session.rollback()
            print("Ocurrio un error en message", e)


        





