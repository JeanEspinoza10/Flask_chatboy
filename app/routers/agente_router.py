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
@agente_ns.doc(security="Bearer")
class Agentes(Resource):
    @jwt_required()
    @role_required(rol_id=2)
    @agente_ns.expect(request_schema.all())
    def get(self):
        '''Listamos los agentes'''
        query = request_schema.all().parse_args()
        controller = AgenteController()
        return controller.all(query)

    @jwt_required()
    @role_required(rol_id=2)
    @agente_ns.expect(request_schema.create(), validate=True)
    def post(self):
        '''Creacion de agentes'''
        controller = AgenteController()
        return controller.create(request.json)
   

@agente_ns.route('/<int:id>')
@agente_ns.doc(security="Bearer")
class UserById(Resource):
    @jwt_required()
    def get(self, id):
        ''' Obtener un agente por el ID '''
        controller = AgenteController()
        return controller.getById(id)
    
    @jwt_required()
    @role_required(rol_id=2)
    @agente_ns.expect(request_schema.update(), validate=True)
    def put(self, id):
        ''' Actualizar un agente por el ID '''
        controller = AgenteController()
        return controller.update(id, request.json)
    
    @jwt_required()
    @role_required(rol_id=2)
    def delete(self, id):
        ''' Inhabilitar un agente por el ID '''
        controller = AgenteController()
        return controller.delete(id)    

@agente_ns.route("/profile/me")
@agente_ns.doc(security="Bearer")
class UserByProfile(Resource):
    @jwt_required()
    def get(self):
        '''Obtener los datos del usuario'''
        controller = AgenteController()
        return controller.profileMe()

