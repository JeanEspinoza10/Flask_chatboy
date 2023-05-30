from flask_restx import fields
from flask_restx.reqparse import RequestParser

class AuthRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace
    
    # Crear usuario
    def signup(self):
        return self.namespace.model("Auth SignUp", {
            "name": fields.String(required=True, min_length=2, max_length=120),
            "correo": fields.String(required=True, min_length=2, max_length=120),
    
        }

        )