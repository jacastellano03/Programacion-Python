# Tarea 19
# Desarrolle un sistema de reservas que controle cupos agotados, cantidades inválidas y usuarios vacíos.

try:

    usuario = input("Ingrese el nombre del usuario: ")

    if usuario == "":
        raise Exception("El usuario no puede estar vacío.")

    cantidad =  int(input('Ingrese la cantidad de cupos a reservar: '))

    if cantidad <= 0:
        raise Exception("Cantidad inválida.")

    cupos = 100

    if cantidad > cupos:
        raise Exception("No hay suficientes cupos.")
    
    cupos -= cantidad
    print('Reserva realizada correctamente.')
    print(f"Cupos restantes: {cupos}")

except ValueError:
    print('Ingrese un número válido.')
    
except Exception as e:
    print(e)