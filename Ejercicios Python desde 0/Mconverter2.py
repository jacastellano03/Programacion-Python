# 2. Crea un módulo llamado "converter" que tenga funciones para convertir temperaturas entre Celsius y Fahrenheit. Escribe un programa que importe este módulo y realice conversiones.



# Celsius -> Farenheit
# Farenheit -> Celsius





def celsius_a_ferenheit(c):
    resultado = (9/5 * c)+ 32
    return resultado

def farenheit_a_celsius(f):
    resultado = (5/9) * (f - 32)                # Pero en Python SIEMPRE necesitas: (5/9) * (f - 32) no olvidarse de los operadores
    return resultado

# print(farenheit_a_celsius(108))
# print(celsius_a_ferenheit(40))