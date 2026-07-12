# Ejercicio de clase 11
# Solicite tres precios y calcule el promedio. Controle errores de conversión.

def promedio_precios():

    try:
        precio1 = float(input("Ingrese el primer precio: "))
        precio2 = float(input("Ingrese el segundo precio: "))
        precio3 = float(input("Ingrese el tercer precio: "))

        promedio = (precio1 + precio2 + precio3) / 3

        print("El promedio es:", promedio)

    except ValueError:
        print("Debe ingresar únicamente valores numéricos.")

promedio_precios()