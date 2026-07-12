# Ejercicio de clase 2
# Solicite dos números y realice una división. Controle `ValueError` y `ZeroDivisionError`.

def division ():
    try:
        num1  = int(input("Ingrese el primer número: "))
        num2  = int(input("Ingrese el segundo número: "))

        resultado = (num1 / num2)
        print(resultado)

    except ValueError:
        print("Debe ingresar un número entero")
    
    except ZeroDivisionError:
        print('Ingresa un numero divisor diferente de 0.')

division()