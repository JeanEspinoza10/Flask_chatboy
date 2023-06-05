from app import db
from app.models.conversation_model import Conversation
from app.models.agente_model import Agentes
from app.utils.time import Fechas


class AsignarController:
    def __init__(self):
        self.conversacion = Conversation
        self.model = Agentes
        self.fechas = Fechas()

    def cargaAgentes(self):
        try:
            agentes_activos = self.model.where(status=True).order_by("id").all()
            carga = []
            
            for agente in agentes_activos:
                carga_agente = len(self.conversacion.where(fecha=self.fechas.fecha()).filter_by(agente_id = agente.id).all())
                new_element = [agente, carga_agente]
                carga.append(new_element)
            
            
            # Ordenar la lista de listas por el segundo elemento de cada elemento
            carga_ordenada = sorted(carga, key=lambda x: x[1])

            return carga_ordenada
        except Exception as e:
            return f"error, {e}"

    def updateAsignacion(self, agente):
        try:
            # Agentes
            lista_agentes = agente
            # Buscando las conversacion donde esten en estado_id = 1 = En proceso
            conversation_proceso = self.conversacion.where(estado_id = 1).order_by("id").all()            
            
            if conversation_proceso:
                for element in conversation_proceso:
                    agente_asignar = lista_agentes[0][0]
                    dataconversation = {
                        "agente_id":agente_asignar.id
                    }
                    element.update(**dataconversation)
                    db.session.add(element)
                    db.session.commit()
                    lista_agentes[0][1] += 1
                    lista_agentes= sorted(lista_agentes, key=lambda x: x[1])  # Volver a ordenar la lista de agentes

        except Exception as e:
            db.session.rollback()
            return e