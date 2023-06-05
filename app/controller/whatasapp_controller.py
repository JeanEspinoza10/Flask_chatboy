from flask import request
import os
from app.utils.obtencion_messages import GetTextUser
from app.utils.generate_messages import GenerateMessage
from app.utils.send_messages import SendMessageWhatsapp
from app.utils.save_data import Save
from app.controller.asignar_controller import AsignarController

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
            #Obteniendo el diccionario
            body = query.get_json()
            entry = (body["entry"])[0]
            changes = (entry["changes"])[0]
            value = (changes["value"])
            message = (value["messages"])[0]
            number = message["from"]
            time = message["timestamp"]
            contacts = (value["contacts"])[0]
            ws_id = (contacts["wa_id"])
            text, tipo = GetTextUser(message)
            contacts = (value["contacts"])[0]
            profile = contacts["profile"]   
            name = profile["name"]

            # Inicializando la clase grabar
            update = Save()

            # Tabla de personal
            update.personal(name, number)
            # Tabla de message
            update.message(text, tipo, number,time)
            
            #Asignacion de la conversacion
            asignar = AsignarController()
            carga = asignar.cargaAgentes()
            
            # Subir cambios
            result = asignar.updateAsignacion(carga)
            
               
            # Obtencion del formato de envio
            data = GenerateMessage(text, number, name)
            
            for dato in data:
                # Envio de mensaje
                enviar = SendMessageWhatsapp(data=dato)

            return "EVENT_RECEIVED"
        except Exception as e:
            print("Error recibir", e)
            return "EVENT_RECEIVED"