from app import api
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.helpers.decorators import role_required

send_ns = api.namespace(
    name = "Envio de mensajes",
    description ="Rutas para envio de mensaje",
    path = "/sendmessages"

)


