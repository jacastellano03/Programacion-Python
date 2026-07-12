# Ejercicio de clase 4
# Cree una función que reciba una nota y lance ValueError si no está entre 0 y 100.

def validar_nota():

    try:
        nota = int(input("Ingrese una nota: "))

        if nota < 0 or nota > 100:
            raise ValueError("La nota debe estar entre 0 y 100.")

        print("Nota válida:", nota)

    except ValueError as e:
        print(e)

validar_nota()