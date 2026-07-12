# Ejercicio de clase 8
# Cree una calculadora que permita sumar, restar, multiplicar y dividir, controlando entradas inválidas.

def calculadora():

    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))

        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            print("Resultado:", num1 + num2)

        elif opcion == 2:
            print("Resultado:", num1 - num2)

        elif opcion == 3:
            print("Resultado:", num1 * num2)

        elif opcion == 4:
            print("Resultado:", num1 / num2)

        else:
            print("Opción no válida.")

    except ValueError:
        print("Debe ingresar únicamente números enteros.")

    except ZeroDivisionError:
        print("No se puede dividir entre cero.")

calculadora()