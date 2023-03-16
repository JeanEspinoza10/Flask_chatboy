def ListaOpciones(number, name):
    # Obtener los datos de la base de datos y enviarlo mediante whatsapp.
    data =  {
            "messaging_product": "whatsapp",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "body": {
                    "text": f"*Hola,{name}.Tenemos estas opciones:* 😊"
                },
                "footer": {
                    "text": "Selecion alguna de estas opciones"
                },
                "action": {
                    "button": "Observar",
                    "sections": [
                        {
                            "title": f"✍Procesos✍",
                            "rows": [
                                {
                                    "id": "main-ticket",
                                    "title": "Ticket",
                                    "description": "Creacion de ticket de atencion"
                                },
                                {
                                    "id": "main-red",
                                    "title": "Usuario de red",
                                    "description": "Varios"
                                }
                            ]
                        },
                        {
                            "title": f"✍Contacto✍",
                            "rows": [
                                {
                                    "id": "main-soporte",
                                    "title": "Agente",
                                    "description": "Mesa de servicios"
                                },
                                {
                                    "id": "main-correo",
                                    "title": "Correo",
                                    "description": ""
                                }
                            ]
                        }
                    ]
                }
            }
}


    return data