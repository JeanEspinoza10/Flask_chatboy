def TextPresentacion(number, name):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "text",
            "text": {
                "body": f"*Hola,{name}.Tenemos estas opciones:* 😊"
                }
        }

    return data


