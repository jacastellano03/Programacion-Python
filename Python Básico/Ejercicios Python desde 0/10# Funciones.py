### FUNCTIONS ###

"""
Las funciones son bloques de código reutilizables que nos permiten organizar nuestro 
código de manera eficiente, reducir la repetición y hacerlo más legible y fácil de 
mantener. Las funciones nos permiten dividir grandes programas en pequeñas piezas 
manejables, facilitando la comprensión y el mantenimiento de nuestro código.

Las funciones son esenciales porque te permiten escribir código que es reutilizable 
y modular. En lugar de repetir el mismo código una y otra vez, puedes encapsularlo 
dentro de una función y llamarlo siempre que lo necesites. Esto hace que tu programa 
sea más organizado y fácil de entender.

palabra reservada --> def

"""

def my_function ():
    print('Como antes como cuando no era cantante')

my_function()
my_function()
my_function()

def sum_two_values (first_number, second_number):       # Aqui colocamos los parametros
    print(first_number + second_number)

sum_two_values(50, 50)
sum_two_values(133, 67)
sum_two_values(1516561, 651651)
sum_two_values("5","7")             #Solo une las cadenas de texto no las suma
sum_two_values(3.4, 5.7)


def sum_two_values_with_return (first_value, second_value):
    return first_value + second_value

my_result = sum_two_values_with_return(10, 5)
print(my_result)

my_result = sum_two_values_with_return(3.4, 5.2)
print(my_result)


def print_name (name, surname):
    print(f"{name} {surname}")

print_name("Alejandro", "Castellano")


def print_name_with_default (name, surname, alias = "Sin alias"):          # Por defecto se colocará sin alias, si no le damos un valor toma el valor por defecto
    print(f"{name} {surname} {alias}")

print_name_with_default("Alejandro", "Castellano", "Niño")

print_name_with_default("Nayeli", "Castellano")

def print_texts (*texts):
    print(texts)
    

print_texts("Hi", "Python", "Castellano")
print_texts("Hi", "Python")
print_texts("Hi")



def print_texts (*texts):
    for text in texts:
        print(text.upper())
    print(texts)

print_texts("Hi", "Python", "Castellano")



#EXCERCICES.PY10``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

print("EJERCICIOS")


print("Exercise 1")
# 1. Crea una función llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>". Si no se proporciona ningún nombre, debe saludar diciendo "Hola, desconocido".

def personalized_greeting (name = "desconocido"):
    print("Hola", f"{name}")

personalized_greeting()
personalized_greeting("Azael")



print("Exercise 2")
# 2. Escribe una función llamada "multiply" que reciba dos números como argumentos y retorne el resultado de multiplicarlos.

def multiply(first_number, second_number):
    print(first_number * second_number)

multiply(4, 4)
multiply(8, 8)
multiply(4, 5)



print("Exercise 3")
# 3. Crea una función llamada "is_even" que reciba un número entero como argumento y retorne True si es par y False si es impar.

def is_even(number):
    if number %2 == 0:
        return True
    else:
        return False

print(is_even(14))
print(is_even(3))

print("Example")
# Función para saber si un número es positivo

def is_positive (num):
    return num %2 == 0

print(is_positive(5))
print(is_positive(64))


print("Example")
# Función para saber si un número es múltiplo de 5

def is_multiple_of_five (num):
    return num %5 == 0

print(is_multiple_of_five(50))
print(is_multiple_of_five(14))


print("Example")
# Función que devuelva el número mayor entre dos

def max_number(a,b):
    if a > b:
        return a
    else:
        return b
    
print(max_number(10,8))
print(max_number(400,820))
print(max_number(-200,0))


print("Example")
# Función que calcule el cuadrado de un número

def square(num):
    return num * num

print(square(8))
print(square(4))
print(square(3))


print("Example")
# Función que diga si un número es mayor que 100

def greater_than_100 (num):
    return num > 100

print(greater_than_100(99))
print(greater_than_100(400))
print(greater_than_100(69))



print("Exercise 4")
# 4. Escribe una función llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayúsculas.

def convert_to_uppercase(text):
        print(text.upper())

convert_to_uppercase("hola")
convert_to_uppercase("hola amor como vas te extranio")



print("Exercise 5")
# 5. Crea una función llamada "arbitrary_sum" que reciba un número arbitrario de números como argumentos y retorne la suma de todos ellos.

def arbitrary_sum(*numbers):
    return sum(numbers)

print(arbitrary_sum(18,12))
print(arbitrary_sum(14,24))
print(arbitrary_sum(1,12))
print(arbitrary_sum(8,42))



print("Exercise 6")
# 6. Escribe una función llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.

def generate_full_greeting(name, surname):
    print("Hola", f"{name} {surname}")

generate_full_greeting("Jhoel", "Castellano")


def codiko(name, age):
    print("Hola", f"{name} {age}")

codiko('Stalin', "24")

def generate_full_greeting (name = "Sin nombre", surname = "Sin apellido", age = "Sin edad"):
    print("Klk mi loco", f"{name} {surname} {age}")

generate_full_greeting()
generate_full_greeting('Niño', 'Jazz', 23)



print("Exercise 7")
# 7. Crea una función llamada "power" que reciba dos números: base y exponente, y retorne el resultado de elevar la base al exponente.

def power(first_number_base, second_number_exp):                                
    return first_number_base ** second_number_exp                       # Para elevar un numero al exponente se coloca (**)

print(power(5, 6))
print(power(2, 4))
print(power(4, 3))



print("Exercise 8")
# 8. Escribe una función llamada "calculate_average" que reciba tres números y retorne su promedio.

def calculate_average(first_number, second_number, three_number):
    return (first_number + second_number + three_number) / 3                # Es importante colocar los numeros como si estuvieramos en matematicas reales es decir se sigue un orden igual o similar se usan los parentesis para separar o unir operaciones 

print(calculate_average(10, 14, 18))
print(calculate_average(14, 13, 18))
print(calculate_average(10, 10, 18))



print("Exercise 9")
# 9. Crea una función llamada "count_characters" que reciba una cadena de texto y retorne el número de caracteres que contiene.

def count_characters(string):
    return len(string)                               # len() cuenta el numero de caracteres total y count un numero de caracteres que se repiten pero solo de los mismos

print(count_characters("Hola Amor Como Estas"))

def counting(texts):
    return len(texts)

print(counting('KELOKE MMGV QUE DICEN LAS BARBBIES'))

def klklklk(jljljlj):
    return len(jljljlj)

print(klklklk("sjfkafbkjafbuawkfbka"))

def contar_caracteres(texto):
    return len(texto)

print(contar_caracteres("Sorra estupida bastarda te amo Danny Flowww"))



print("Exercise 10")
#10. Escribe una función llamada "display_messages" que reciba un número indefinido de cadenas y las imprima en mayúsculas, una por una, tal como se hizo en el archivo proporcionado.

def display_messages(*texts):
    for texts in texts:                     # Es importante que se coloque el for text in text  para poder hacer que la funcion imprima si o si
        print(texts.upper())

display_messages("Hola beba")
display_messages("can your say text me to paradise")
display_messages("cause you make me feel like")

def display_messages1 (*pretextos):
    for pretextos in pretextos:
        print(pretextos.capitalize())

display_messages1("me gustan los bares y las develadas lunes a domingo y toda la semana")
display_messages1("es un secreto que tu mirada y la mia un PRESENTIMIENTO")
display_messages1("TU SABES QUE NACISTE PA MI")


def display_messages2(*billete):
    for billete in billete:
        print(billete.lower())

display_messages2("TODO LO QUE NOS PROMETIMOS SE QUEDO EN EL ACTO EN BRICKELL")
display_messages2("FLASHES DE PELICULA")
display_messages2("BOLSA EXOTICA TACONES Y CURVA SOLIDA")




