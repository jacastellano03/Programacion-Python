# Tarea 4
# Cree un programa que consulte productos en un diccionario y controle claves inexistentes.

productos = {
    'arroz': 2.50,
    'leche': 1.20,
    'pan': 0.50
}

producto = input('Ingrese el producto: ')
# print(productos[producto])

try:
    print(productos[producto])
    
except KeyError as e:
    print('El producto no existe en el diccionario')