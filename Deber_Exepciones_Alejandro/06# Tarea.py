# Tarea 6
# Cree una función que calcule el promedio de una lista. Lance una excepción si la lista está vacía.

lista = [10,20,30]

def promedio(lista):
    
    if lista == []:
        raise ValueError('La lista está vacía.')
    
    suma = sum(lista)
    cantidad = len(lista)
    
    promedio = suma/cantidad
    print(promedio)

promedio(lista)