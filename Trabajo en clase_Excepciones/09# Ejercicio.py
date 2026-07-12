# Ejercicio de clase 9
# Abra un archivo llamado notas.txt y controle FileNotFoundError.

def abrir_archivo():

    try:
        with open("notas.txt", "r") as archivo:

            contenido = archivo.read()
            print(contenido)

    except FileNotFoundError:
        print("El archivo notas.txt no existe.")

abrir_archivo()