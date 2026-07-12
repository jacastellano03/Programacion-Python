# Ejercicio de clase 5
# Solicite una posición de una lista de videojuegos y controle IndexError.

def videojuegos():

    lista_videojuegos = ["Minecraft", "Free Fire", "FIFA", "Call of Duty", "GTA V"]

    try:
        posicion = int(input("Ingrese una posición: "))

        print("Videojuego:", lista_videojuegos[posicion])

    except IndexError:
        print("La posición ingresada está fuera de la lista.")

    except ValueError:
        print("Debe ingresar un número entero.")

videojuegos()