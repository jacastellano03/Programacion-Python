# Ejercicio de clase 14
# Solicite una contraseña y lance una excepción si tiene menos de 8 caracteres.

def validar_contrasena():

    try:
        contrasena = input("Ingrese una contraseña: ")

        if len(contrasena) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres.")

        print("Contraseña válida.")

    except ValueError as e:
        print(e)

validar_contrasena()