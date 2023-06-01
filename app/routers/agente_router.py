from app import api
from flask_restx import Resource
from flask import request
from flask_jwt_extended import jwt_required
from app.helpers.decorators import role_required
from app.controller.agente_controller import AgenteController
from app.schemas.agente_schemas import AgentesRequestSchema

agente_ns = api.namespace(
    name='Agentes',
    description='Rutas del modulo Agentes',
    path='/agentes'
)

request_schema = AgentesRequestSchema(agente_ns)

# Creando las rutas
@agente_ns.route("")
class Agentes(Resource):
    @agente_ns.expect(request_schema.all())
    def get(self):
        '''Listamos los usuarios'''
        query = request_schema.all().parse_args()
        controller = AgenteController()
        return controller.all(query)

    @agente_ns.expect(request_schema.create(), validate=True)
    def post(self):
        '''Creacion de usuarios'''
        controller = AgenteController()
        return controller.create(request.json)

   

@agente_ns.route('/<int:id>')
class UserById(Resource):
    def get(self, id):
        ''' Obtener un usuario por el ID '''
        controller = AgenteController()
        return controller.getById(id)
    
    
    @agente_ns.expect(request_schema.update(), validate=True)
    def put(self, id):
        ''' Actualizar un usuario por el ID '''
        controller = AgenteController()
        return controller.update(id, request.json)
    
    def delete(self, id):
        ''' Inhabilitar un usuario por el ID '''
        controller = AgenteController()
        return controller.delete(id)    