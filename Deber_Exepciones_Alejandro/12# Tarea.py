# Tarea 12
# Desarrolle un sistema de registro de notas usando diccionarios y controle estudiantes inexistentes.

diccionario = {
    "Juan": 9,
    "Ana": 10,
    "Pedro": 8
}

try:
    nombre = input('Ingrese el nombre del estudiante: ')

    if nombre not in diccionario:
        raise Exception ("El estudiante no existe.")

    print(diccionario[nombre])

except Exception as e:
    print(e)