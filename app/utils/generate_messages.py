from app.plantillas.bienvenida_messages import TextPresentacion
def GenerateMessage(messageUser, number, name):
    data = None
    data = TextPresentacion(number, name)
    return data
    
