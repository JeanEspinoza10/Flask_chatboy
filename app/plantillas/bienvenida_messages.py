def TextPresentacion(number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "text",
            "text": {
                "body": "Hola, buenas tardes. Puede brindarnos los siguientes datos: 1) Nombre y apellidos 2) Correo"
                }
        }
    
    return data

