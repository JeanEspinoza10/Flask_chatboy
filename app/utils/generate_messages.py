from app.plantillas import bienvenida_messages, listaopciones_messages
def GenerateMessage(messageUser, number, name):
    data = None
    #data = TextPresentacion(number, name)
    data = listaopciones_messages.ListaOpciones(number, name)
    return data
    
