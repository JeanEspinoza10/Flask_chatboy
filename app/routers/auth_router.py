from app import api
from flask_restx import Resource
from flask import request
from app.schemas.auth_schemas import AuthRequestSchema
from app.controller.auth_controller import AuthController

auth_ns = api.namespace(
    name= "Autenticacion",
    description = "Rutas del modulo de Autenticacion",
    path="/auth"
)

request_schema = AuthRequestSchema(auth_ns)

# Crando las rutas del servicio
@auth_ns.route("/signin")
class SignIn(Resource):
    @auth_ns.expect(request_schema.signin(),validate=True)
    def post(self):
        "Login de agentes"
        controller = AuthController()
        return controller.signIn(request.json)

@auth_ns.route('/signup')
class SignUp(Resource):
    @auth_ns.expect(request_schema.signup(), validate=True)
    def post(self):
        ''' Registro de agentes '''
        controller = AuthController()
        return controller.signUp(request.json)

