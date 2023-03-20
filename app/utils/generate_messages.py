from app.plantillas import bienvenida_messages, listaopciones_messages, tickets_messages

def GenerateMessage(messageUser, number, name):
    
    messageUser = messageUser.lower()
    data = None
    
    if "1" in messageUser:
        data = tickets_messages.OpcionOne(messageUser, number, name)
        return data
    if "crear ticket" in messageUser:
        data = tickets_messages.CrearTicket(messageUser, number, name)
        return data

    if "seguimiento ticket" in messageUser:
        data = tickets_messages.SeguimientoTicket(messageUser, number, name)
        return data

    

    data = bienvenida_messages.TextPresentacion(number, name)
    return data
    
