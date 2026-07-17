# Tarea 9
# Cree un conversor de temperatura que controle opciones inválidas y entradas no numéricas.

opcion = int(input('Seleccione una opción:\n1. Celsius a Fahrenheit\n2. Fahrenheit a Celsius\nOpción: '))

if opcion != 1 and opcion != 2:
    raise Exception('Opción inválida.')

try:
    temperatura = float(input('Ingrese la temperatura: '))
    
    if opcion == 1:
        farenheit = (temperatura * 9/5) + 32
        print(f"La temperatura en Fahrenheit es: {farenheit} °F")
    
    elif opcion == 2:
        celsius = (temperatura - 32) * 5/9
        print(f"La temperatura en Celsius es: {celsius} °C")

except ValueError:
    print('Ingrese una temperatura válida.')