# Ejercicio de clase 7
# Solicite una cantidad positiva usando while, try, except y raise.

def cantidad_positiva():

    while True:

        try:
            cantidad = int(input("Ingrese una cantidad positiva: "))

            if cantidad <= 0:
                raise ValueError("La cantidad debe ser positiva.")

            print("Cantidad válida:", cantidad)
            break

        except ValueError as e:
            print(e)

cantidad_positiva()