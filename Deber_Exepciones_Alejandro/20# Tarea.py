# Tarea 20
# Cree un programa integrador que lea datos desde un archivo, procese números y genere un resumen; controle archivo inexistente, datos inválidos y divisiones para cero.

try:
    archivo = open("datos.txt", "r")
    datos = archivo.read()
    
    datos = datos.splitlines()
    
    suma = 0
    contador = 0
    
    for dato in datos:              #recorrer esa lista con un for para convertir cada elemento a número
        numero = int(dato)
        suma += numero
        contador += 1
    
    promedio = suma / contador
    
    print(f'Suma: {suma}')
    print(f'Cantidad de datos: {contador}')
    print(f'Promedio: {promedio}')
    
    
except FileNotFoundError:
    print("El archivo no existe.")
    
except ValueError:
    print("El archivo contiene datos inválidos.")
    
except ZeroDivisionError:
    print("No se puede dividir para cero.")