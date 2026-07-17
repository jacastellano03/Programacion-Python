# Tarea 2
# Cree una función que calcule el área de un triángulo y lance una excepción si base o altura no son positivas.

def area_triangulo():
    
    try:
        base = float(input('Ingrese la base del triangulo: '))
        altura = float(input('Ingrese la altura del triangulo: '))
        
        if base <= 0 or altura <= 0:
            raise ValueError('La base y la altura deben ser mayores que cero.')
        
        area_triangulo = (base * altura)/2
        
        print("El área del triángulo es:", area_triangulo)
        
    except ValueError as e:
        print(e)
        
area_triangulo()