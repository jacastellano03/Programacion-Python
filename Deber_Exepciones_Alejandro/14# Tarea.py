# Tarea 14
# Cree un programa que calcule potencias y controle exponentes no enteros.


try:
    base = int(input('Ingrese la base de la potencia: '))
    exponente = int(input('Ingrese el exponente de la potencia: '))
    
    potencia = base ** exponente
    print(f'El resultado de la potencia es: {potencia}')
    
except ValueError:
    print("Ingrese un número entero.")
    
