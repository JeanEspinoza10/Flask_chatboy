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
    # Crear ticket de atencion con Proactiva
    data = []
    data_presentacion = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "text",
            "text": {
                "body": f"Por favor brindenos los siguientes datos, con el siguiente formato:"
                },
                
        }
    data_informacion = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "text",
            "text": {
                "body": f" 1) Nombre y Apellidos\n2) Correo ✉\n3) Telefono de contacto ☎"
                },
                
        }
       
    data.append(data_presentacion)
    data.append(data_informacion)
    return data

def SeguimientoTicket(messag, number, name):
    pass
