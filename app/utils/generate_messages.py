from app.plantillas.bienvenida_messages import TextPresentacion
def GenerateMessage(messageUser, number):
    data = None
    data = TextPresentacion(number)
    return data
    
