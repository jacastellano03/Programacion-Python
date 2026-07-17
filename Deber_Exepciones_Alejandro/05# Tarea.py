# Tarea 5 
# Solicite una ruta de archivo y muestre su contenido. Controle archivo inexistente y problemas de lectura.

ruta = input('Ingrese la ruta del archivo: ')

try:
    with open(ruta, 'r') as archivo:
        
        contenido = archivo.read()
        print(contenido)
    
except FileNotFoundError:
    print('El archivo no se pudo encontrar.')
    
except PermissionError:
    print('No tiene permisos para leer el archivo.')