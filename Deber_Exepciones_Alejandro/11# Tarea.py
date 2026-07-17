# Tarea 11
# Cree una función que busque un valor en una lista y lance una excepción personalizada si no existe.

lista = [10, 20, 30, 40, 50]

class ValorNoEncontrado(Exception):
    pass

def buscar(lista, valor):
    
    if valor not in lista:
        raise ValorNoEncontrado('El valor no existe en la lista.')

try:
    valor = int(input("Ingrese el valor a buscar: "))
    buscar(lista, 100)
    
except ValorNoEncontrado as e:
    print(e)