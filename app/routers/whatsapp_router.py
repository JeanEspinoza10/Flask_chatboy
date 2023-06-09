from app import api
from flask_restx import Resource
from flask import request
from app.controller.whatasapp_controller import Webhook
import os
from dotenv import load_dotenv


webhook_ns = api.namespace(
    name="Webhook",
    description="Ruta para recibir y enviar",
    path ="/whatsapp"
)

load_dotenv()

@webhook_ns.route("")
class Whatsapp(Resource):
    def get(self):
        query = request
        controller = Webhook
        return controller.VerifyToken(query)
    def post(self):
        query = request
        controller = Webhook
        return controller.ReceiverMessage(query)


