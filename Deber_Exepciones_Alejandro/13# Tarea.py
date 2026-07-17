# Tarea 13
# Solicite números hasta reunir cinco valores válidos. Ignore entradas incorrectas sin detener el programa.

lista = []
contador = 0

while contador < 5:
    try:
        numero = int(input("Ingrese un número: "))
        lista.append(numero)
        contador += 1                                       #contador = contador + 1
        
    except ValueError:
        print("Ingrese un número válido.")
        
print(lista)