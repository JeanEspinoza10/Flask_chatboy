from flask import request
import os


class Webhook:
    def VerifyToken(query):
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
    
    def ReceiverMessage(query):
        try:
            #Obtener el texto y el numero telefonico
            body = query.get_json()
            entry = (body["entry"])[0]
            changes = (entry["changes"])[0]
            value = (changes["value"])
            message = (value["messages"])[0]
            number = message["from"]
            print(number)

            return "EVENT_RECEIVED"
        except Exception as e:
            print("Error 1", e)
            return "EVENT_RECEIVED"