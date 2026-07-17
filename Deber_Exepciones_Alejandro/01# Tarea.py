# Tarea 1
# Solicite el año de nacimiento y calcule la edad. Controle valores no numéricos y años futuros.

def birth_date():
    
    try:
        birth_date = int(input('Ingrese su fecha de nacimiento: '))
        
        if birth_date > 2026:
            print("Ingrese una fecha de nacimiento válida.")
            
            from datetime import datetime
        
        else:
            año_actual = datetime.now().year
            edad = año_actual - birth_date
            print('Su edad es:', edad)
            
    except ValueError as stringserrors:
        
        if 'invalid literal' in str(stringserrors):
            print('Debe ingresar un número entero.')
        
birth_date()