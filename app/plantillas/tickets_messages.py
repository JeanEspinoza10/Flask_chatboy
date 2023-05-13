from app.models.datos_model import Datos
from app import db
from app.plantillas.servicios_messages import Servicios

def TextFormatMessage(text, number):
    data = []
    data_message = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "text",
            "text": {
                "body": f"{text}"
                }
        }
    data.append(data_message)
    return data


def OpcionOne(message, number, name):
    data =[]
    data_opciones = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": f"{number}",
            "type": "interactive",
            "interactive": {
                    "type": "button",
                    "body": {
                        "text": "*A continuacion se muestra las acciones a realizar:*"
                    },
                    "action": {
                        "buttons": [
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "unique_1",
                                    "title": "Crear Ticket ✍"
                                }
                            },
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "unique_2",
                                    "title": "Seguimiento Ticket 🔍 "
                                }
                            }
                        ]
                    }
                }
            }

    data.append(data_opciones)
    
    return data

def CrearTicket(message, number, name):
    # Buscando datos en mi tabla de datos_como mejora
    try:
        pass
    except:
        pass
    return 

def SeguimientoTicket(messag, number, name):
    pass

def Obteniendodatos(messag, number):
    try:
        cadena = messag
        nombre, correo = cadena.split("2)")[0].strip().replace("1)", ""), cadena.split("2)")[1].strip()
        data = {
            "name": nombre,
            "phone":number,
            "correo": correo
        }
        # Grabando datos en la tabla
        usuarios = Datos(**data)
        db.session.add(usuarios)
        db.session.commit()

        respuesta = "Su informacion fue registrado correctamente"
        data = TextFormatMessage(respuesta, number)
        respuesta_oficina = "*Complete la siguiente informacion, con el formato*:\n*Oficina:*"
        data_oficina = TextFormatMessage(respuesta_oficina, number)
        data.append(data_oficina[0])
        return data
    except Exception as e:
        respuesta = "Ya tenemos registrado sus datos"
        data = TextFormatMessage(respuesta,number)
        respuesta_oficina = "Complete la siguiente informacion, con el formato:\n*Oficina:*"
        data_oficina = TextFormatMessage(respuesta_oficina, number)
        data.append(data_oficina[0])
        return data

def Oficina(messag, number):
    
    try:
        oficina = messag.split(":")[1]
        data ={
        "oficina": oficina
        }
        record = Datos.where(phone=number).first()
        if record:
            record.update(**data)
            db.session.add(record)
            db.session.commit()
            # Respuesta
            data_servicios = Servicios(number)
            respuesta = "La informacion fue registrado correctamente "
            data_resp = TextFormatMessage(respuesta, number)
            data_servicios.insert(0,data_resp[0])
            return data_servicios

        respuesta = "Brindenos correctamente su oficina:"
        data_resp = TextFormatMessage(data, number)
        return data_resp
    except Exception as e:
        respuesta = "Brindenos correctamente su oficina:"
        data_resp = TextFormatMessage(respuesta, number)
        return data_resp