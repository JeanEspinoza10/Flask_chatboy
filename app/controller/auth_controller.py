from app import db
from app.models.agente_model import Agentes

class AuthController:
    def __init__(self):
        self.model = Agentes
        self.rol_id = 2
    
    

    def signUp(self, data):
        try:
            pass
        except Exception as e:
            return {
                "message": "Ocurrio un error",
                "error": str(e)
            }, 500