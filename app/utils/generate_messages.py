from app.plantillas import bienvenida_messages, listaopciones_messages, tickets_messages
import re
def GenerateMessage(messageUser, number, name):
    
    messageUser = messageUser.lower()
    data = None

               
    if "1)" in messageUser:
        data = tickets_messages.Obteniendodatos(messageUser, number)        
        return data
    elif "a" == messageUser:
        data = tickets_messages.OpcionOne(messageUser, number, name)
        return data
    elif "oficina" in messageUser:
        data = tickets_messages.Oficina(messageUser, number)
        return data
    elif "crear ticket" in messageUser:
        data = tickets_messages.CrearTicket(messageUser, number, name)
        return data
    elif "seguimiento ticket" in messageUser:
        data = tickets_messages.SeguimientoTicket(messageUser, number, name)
        return data
    else:
        data = bienvenida_messages.TextPresentacion(number, name)
        return data



    
    
    
