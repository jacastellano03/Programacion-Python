# Ejercicio de clase 12
# Solicite un índice y elimine un elemento de una lista. Controle ValueError e IndexError.

def eliminar_elemento():

    lista = ["Mario", "Zelda", "Minecraft", "FIFA", "Free Fire"]

    try:
        indice = int(input("Ingrese un índice: "))

        lista.pop(indice)

        print("Elemento eliminado correctamente.")
        print(lista)

    except ValueError:
        print("Debe ingresar un número entero.")

    except IndexError:
        print("El índice está fuera del rango de la lista.")

eliminar_elemento()