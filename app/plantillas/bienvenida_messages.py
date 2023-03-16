def TextPresentacion(number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "text",
            "text": {
                "body": "*Hola, buenas tardes* 😊"
                }
        }
    
    return data

