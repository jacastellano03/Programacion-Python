
import datetime                             # Funcion para calcular la fecha actual

def fecha_actual():
    fecha = datetime.datetime.now()
    
    return fecha




def diferencia_fechas(fecha1, fecha2):      # Funcion para calcular la diferencia entre fechas
    diferencia = fecha1 - fecha2
    
    return diferencia