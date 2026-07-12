# Ejercicio de clase 15
# Cree un programa que lea números hasta que el usuario escriba "fin";
# controle entradas no válidas sin detener el programa.

def leer_numeros():

    while True:

        dato = input("Ingrese un número o escriba 'fin' para salir: ")

        if dato.lower() == "fin":
            print("Programa finalizado.")
            break

        try:
            numero = int(dato)
            print("Número ingresado:", numero)

        except ValueError:
            print("Entrada no válida. Intente nuevamente.")

leer_numeros()