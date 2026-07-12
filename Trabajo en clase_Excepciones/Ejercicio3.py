# Ejercicio de clase 3
# Solicite una edad y lance una excepción si es menor que 0 o mayor que 120.

def perdir_edad ():
    try:
        edad = int(input('Ingrese su edad: '))

        if edad < 0 and edad > 120:
            raise ValueError('Ingrese una edad entre 0 y 120 años.')
        
        print("Edad válida:", edad)
    except ValueError as e:
        print(e)
    
perdir_edad()