# Tarea 17
# Solicite un correo electrónico y lance una excepción si no contiene `@` o `.`.

try:
    correo = input("Ingrese su correo electrónico: ")

    if '@' not in correo or '.' not in correo:
        raise Exception("Correo electrónico inválido.")
    
except Exception as e:
    print(e)
    
    