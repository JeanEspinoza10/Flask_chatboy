from app import api
from flask_restx import Resource
from flask import request
from app.schemas.auth_schemas import AuthRequestSchema
from app.controller.auth_controller import AuthController
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.helpers.decorators import role_required


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
@auth_ns.doc(security="Bearer")
class SignUp(Resource):
    @role_required(rol_id=2)
    @auth_ns.expect(request_schema.signup(), validate=True)
    def post(self):
        ''' Registro de agentes '''
        controller = AuthController()
        return controller.signUp(request.json)

@auth_ns.route("/token/refresh")
class TokenRefresh(Resource):
    @jwt_required(refresh=True)
    @auth_ns.expect(request_schema.refreshToken())
    def post(self):
        '''Obtener un nuevo acces token del refresh token'''
        identity = get_jwt_identity()
        controller = AuthController()
        return controller.refreshToken(identity)


