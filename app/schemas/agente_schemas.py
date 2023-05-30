from flask_restx import fields
from flask_restx.reqparse import RequestParser
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow.fields import Nested
from app.models.agente_model import Agentes

class AgentesRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace
    
    def all(self):
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=5, location='args')
        return parser
    
    # Creando agentes
    def create(self):
        return self.namespace.model("Agente Create",
        {
            "name": fields.String(required=True, max_length=120),
            "correo": fields.String(required=True, max_length=120),
            "password": fields.String(required=True, max_length=120),
            "role_id": fields.Integer(required=True)
        })
    def update(self):
        return self.namespace.model('Agente Update', {
            'name': fields.String(required=False, max_length=80),
            'correo': fields.String(required=False, max_length=120),
            'password': fields.String(required=False, max_length=80),
            'role_id': fields.Integer(required=False)
        })


class AgentesResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Agentes
        ordered = True
        exclude = ['password']

    #role = Nested('RolesResponseSchema', exclude=['agentes'], many=False)
