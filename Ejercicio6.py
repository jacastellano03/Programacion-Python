# Ejercicio de clase 6
# Solicite una clave de un diccionario de estudiante y controle KeyError.

def estudiante():

    diccionario_estudiante = {
        "nombre": "Jhoel",
        "edad": 22,
        "carrera": "Software",
        "universidad": "PUCE"
    }

    try:
        clave = input("Ingrese una clave: ")

        print(diccionario_estudiante[clave])

    except KeyError:
        print("La clave ingresada no existe.")

estudiante()