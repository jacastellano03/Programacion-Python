# Tarea 18
# Cree una función que reciba una lista y un índice, y controle índices negativos o inexistentes.

lista = [10, 20, 30, 40, 50]

def buscar(lista, indice):
    if indice < 0:
        raise Exception('Índice negativo.')
    
    if indice >= len(lista):
        raise Exception("Índice inexistente.")
    
    print('El valor del indice en la lista es:',lista[indice])
    
try:
    indice = int(input('Ingrese un índice: '))
    buscar(lista, indice)

except Exception as e:
    print(e)