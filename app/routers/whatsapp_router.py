from app import api
from flask_restx import Resource
from flask import request
from app.controller.whatasapp_controller import Webhook
import os
webhook_ns = api.namespace(
    name="Webhook",
    description="Ruta para recibir y enviar",
    path ="/whatsapp"
)

@webhook_ns.route("")
class Whatsapp(Resource):
    def get(self):
        query = request
        try:
            accessToken = os.getenv("ACCES_TOKEN")
            token = query.args.get("hub.verify_token")
            challenge = query.args.get("hub.challenge")
            suscribe=query.args.get("hub.mode")
            if token == accessToken:
                return challenge
            else:
                return "No se valido correctamente", 400
        except: 
            return"Error", 400
    def post(self):
        query = request
        controller = Webhook
        return controller.ReceiverMessage(query)