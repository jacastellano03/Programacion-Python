# Ejercicio de clase 1
# Solicite un número entero y muestre su cuadrado. Controle entradas no numéricas.

def cuadrado_numero():

    try:
        numero = int(input("Ingrese un número entero: "))

        cuadrado = numero ** 2
        print("El cuadrado es:", cuadrado)

    except ValueError:
        print("Debe ingresar un número entero")

cuadrado_numero()