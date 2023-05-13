def TextPresentacion(number, name):
    data = []
    
    data_presentacion = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "text",
            "text": {
                "body": f"Bienvenido, *{name}* a Migraciones, estamos aquí para ayudar en temas realacionados con el servicio de tecnologias de la informacion.¿En que podemos ayudarte?😊"
                },
                
        }

    data_datos = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "text",
            "text": {
                "body": f"Puede brindarnos los siguientes datos:\n1) Nombre\n2) Correo ✉\n"
                },
                
        }
    
    



    data.append(data_presentacion)
    data.append(data_datos)

    return data


