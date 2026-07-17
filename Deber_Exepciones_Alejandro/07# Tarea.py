# Tarea 7
# Solicite un nombre de usuario y lance una excepción si contiene espacios o tiene menos de cuatro caracteres.


usuario = input('Ingrese el nombre de usuario: ')

if ' ' in usuario:
    raise ValueError('El usuario no puede contener espacios.')
if len(usuario) < 4:
    raise ValueError('El usuario debe tener al menos 4 caracteres.')
