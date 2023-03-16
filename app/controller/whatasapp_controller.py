from flask import request
import os
from app.utils.obtencion_messages import GetTextUser
from app.utils.generate_messages import GenerateMessage
from app.utils.send_messages import SendMessageWhatsapp

class Webhook:
    def VerifyToken(query):
        try:
            accessToken = os.environ.get("ACCES_TOKEN")
            token = query.args.get("hub.verify_token")
            challenge = query.args.get("hub.challenge")
            suscribe=query.args.get("hub.mode")
            if token != None and challenge != None and token == accessToken:
                challenge = int(challenge)
                return challenge
            else:
                return "No se valido correctamente", 400
        except: 
            return"Error", 400
    
    def ReceiverMessage(query):
        try:
            
            #Obtener el texto y el numero telefonico
            body = query.get_json()
            entry = (body["entry"])[0]
            changes = (entry["changes"])[0]
            value = (changes["value"])
            message = (value["messages"])[0]
            number = message["from"]
            text = GetTextUser(message)
            print(text, number)
            # Obtener el perfil
            contacts = (value["contacts"])[0]
            profile = contacts["profile"]
            name = profile["name"]
            print(name)
            # Obtencion del formato de envio
            data = GenerateMessage(text, number)
        
            # Envio de mensaje
            enviar = SendMessageWhatsapp(data=data)    

            return "EVENT_RECEIVED"
        except Exception as e:
            print("Error 1", e)
            return "EVENT_RECEIVED"