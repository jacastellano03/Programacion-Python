# Ejercicio de clase 10
# Cree una función que convierta una cadena a entero y devuelva None si no es válida.

def convertir_entero(cadena):

    try:
        return int(cadena)

    except ValueError:
        return None

print(convertir_entero("100"))
print(convertir_entero("25"))
print(convertir_entero("hola"))
print(convertir_entero("Python"))