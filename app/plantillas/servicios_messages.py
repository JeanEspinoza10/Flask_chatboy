def Servicios(number):    
    
    data = []
    data_opciones = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "text",
        "text": {
                "body": f"Marca el numero de la opcion que desea realizar su consulta✍"
                },
    }

    data_marca = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "text",
        "text": {
                "body": f"a) Tickets de atencion 📝\nb) Accesos a sistemas informaticos Migraciones\nc) Accesos a sisteams informaticos Pasaporte\nd) Comunicarse con agente de mesa de serivicios 🕵\ne) Retorno de vaciones ✈"
                },

    }
    
    data.append(data_opciones)
    data.append(data_marca)

    return data