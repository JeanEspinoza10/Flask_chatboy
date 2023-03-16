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
        try:
            accessToken = os.environ.get("ACCES_TOKEN")
            print(accessToken)
            token = query.args.get("hub.verify_token")
            print(token)
            challenge = query.args.get("hub.challenge")
            suscribe=query.args.get("hub.mode")
            if token != None and challenge != None and token == accessToken:
                return challenge
            else:
                return "No se valido correctamente", 400
        except: 
            return"Error", 400
    def post(self):
        query = request
        controller = Webhook
        return controller.ReceiverMessage(query)


