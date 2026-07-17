# Tarea 10
# Solicite una fecha en formato día, mes y año. Controle valores fuera de rango.
'''
try:
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))

    if dia < 1 or dia > 31:       # Lo correcto es usar or porque queremos detectar cualquiera de estos dos casos     
        raise Exception ('Día fuera de rango.')
    elif mes < 1 or mes > 12:
        raise Exception ('"Mes fuera de rango."')
    elif año < 1:
        raise Exception ("Año fuera de rango.")
    
except ValueError:
    print('Ingrese valores numéricos.')
    
except Exception as e:
    print(e)
    
'''
try:
    dia = int(input("Ingrese el día: "))
    if dia < 1 or dia > 31:       # Lo correcto es usar or porque queremos detectar cualquiera de estos dos casos     
        raise Exception ('Día fuera de rango.')
    
    mes = int(input("Ingrese el mes: "))
    if mes < 1 or mes > 12:
        raise Exception ('"Mes fuera de rango."')   
    
    año = int(input("Ingrese el año: "))
    if año < 1:
        raise Exception ("Año fuera de rango.")
    
except ValueError:
    print('Ingrese valores numéricos.')
    
except Exception as e:
    print(e)
    