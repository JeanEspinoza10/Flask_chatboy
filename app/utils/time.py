import datetime

class Fechas():
    def __init__(self):
        self.datetime = datetime

    def transtime(self,time):
        try:
            timestamp = int(time)
            fecha_hora = self.datetime.datetime.fromtimestamp(timestamp)

            # Formatear la salida con segundos y milisegundos
            formato = "%Y-%m-%d %H:%M:%S.%f"
            fecha_hora_detallada = fecha_hora.strftime(formato)
            
            return fecha_hora_detallada

        except Exception as e:
            print(e)

    def fecha(self):
        fechaactual = self.datetime.date.today()
        return fechaactual

