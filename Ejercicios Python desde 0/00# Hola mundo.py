# Esto es un comentario se utiliza el numeral para crear comentarios
# Hola mundo

"""
Cómo imprimir texto en la consola: En Python, utilizamos la función print( para mostrar cualquier información en la consola. 
Esta es una función muy versátil, que te permitirá desde mostrar texto hasta imprimir el resultado de cálculos y variables.

Comentarios en Python: Los comentarios son esenciales para hacer que tu código sea legible y fácil de entender, tanto para ti 
como para otros programadores que lo lean en el futuro. Veremos cómo agregar comentarios de una sola línea usando # 
y comentarios de varias líneas utilizando triples comilla '''texto''' 

Tipos de datos básicos: Python nos permite imprimir y consultar el tipo de cualquier dato, desde cadenas de texto hasta números enteros, 
decimales, y booleanos. Aprenderás a identificar el tipo de dato usando la función type()
"""

print("Hola, Python")

print('Hola, Python')               #Esta tambien es una forma de imprimir un string con una comilla 

"""
Este tambien es
un comentario
entre lineas

"""

'''
Este tambien
es un comentario 
en varias lineas

'''
# Consultar el tipo de dato
print(type("Hola, Python"))   # Tipo "str" cadena de texto
print(type(5))                # Tipo "int" entero
print(type(2.5))              # Tipo "float" decimal
print(type(2 + 3j))           # Tipo "complex" complejo
print(type(True))             # Tipo "bool" verdadero
print(type(False))            # Tipo "bool" falso

print("EJERCICIOS")

print("Exercise 1")

#1. Imprime "¡Hola Mundo!" por consola.

print("Hola, Mundo soy Jhoel Alejandro y me voy a convertir el mas grande de todos")

print("Exercise 2")
#2. Escribe un comentario de una sola línea explicando qué hace el código del Ejercicio 1.

#Este es un comentario de una solo linea en el cual vamos a explicar que hace el primer ejercicio, se esta imprimiendo por consola Hola Mundo utilizando el print, parentesis y comillas.

print("Exercise 3")
#3. Imprime tu nombre y edad en la misma línea utilizando la función print.

my_name = ("Jhoel Alejandro")
my_age = 22
print(my_name)
print(my_age)

print("Exercise 4")
#4. Usa la función type() para imprimir el tipo de dato de una cadena de texto, un número entero y un número decimal.

text_1= ("WestCOL es la cabrita el mas grande streamer de colombia")
my_number= 593
my_number2 = 10.7

print(type(text_1))
print(type(my_number))
print(type(my_number2))

print("Exercise 5")
#5. Escribe un comentario en varias líneas explicando qué son los tipos de datos en Python.

"""
Los tipos de datos en Python definen la naturaleza de los
valores que una variable puede almacenar y cómo se pueden
manipular.

>Numéricos
int: Enteros positivos o negativos sin decimales (ej. 5, -10).
float: Números de coma flotante o decimales (ej. 3.14, -0.01).
complex: Números complejos (ej. 1+2j).

>Texto
str: Cadenas de caracteres alfanuméricos ("Hola Mundo").

>Booleano (lógicos)
bool: Representan verdadero (True) o falso (False).

>Secuencias
list: Colecciones ordenadas y mutables (ej. [1, "a", 3.14]).
tuple: Secuencias ordenadas e inmutables (ej. (1, 2, 3)).
range: Secuencia de números, usualmente usada en bucles.

>Diccionarios
dict: Pares clave-valor desordenados (ej. {"nombre": "Ana", "edad": 25}).

>Conjuntos:
set / frozenset: Colecciones desordenadas de elementos únicos. 

"""

print("Exercise 6")
#6. Imprime el resultado de concatenar dos cadenas de texto, por ejemplo: "Hola" y "Mundo".

text2= ("Hola, ")
text3= ("Mundo")

print(text2)
print(text3)

text123= ("Anuel la ")
text1234= ("doble AA")

print(text123)
print(text1234)

print("Exercise 7")
# 7. Crea una variable para almacenar tu nombre, otra para tu edad, e imprime ambas en la misma línea.

my_variable1=("Jhoel Alejandro ")
my_variable2=("22")

my_name2= my_variable1
my_age2= my_variable2

print(my_name2+my_age2)


def args_1 (name,age):
    print(name,age)

args_1("Jhoel Alejandro","22")

my_dict = {"name":"Jhoel Alejandro", "age":22}                        # Usamos un dicccionario por que es mejor para representar ya que nos da respectivamente el name y age
print(my_dict)


print("Exercise 8")
#8. Escribe un programa que solicite al usuario su nombre y lo imprima junto con un saludo.


print("Exercise 9")
#Usa print() para mostrar el resultado de la suma de dos números enteros y el tipo de dato resultante.

print(f"Suma: 15 + 49 =  {15 + 49 }")
print(type(f"Suma: 15 + 49 =  {15 + 49 }"))

suma = (23 + 46)
print("Suma: 23 + 46 =", (suma))
print("Suma: 23 + 46 =",type(suma))

result= 5 + 8
print("El resultado es:", result)
print("El resultado es:", type(result))

#10. Comenta el código del Ejercicio 9, y explica qué hace cada línea usando comentarios de una sola línea.

#Suma de dos numeros enteros
result= 5 + 8
#Impresion de la suma de los numeros enteros mas un string que dice El resultado es
print("El resultado es:", result)
#Imprime el tipo de dato del resultado, que es 'int'.
print("El resultado es:", type(result))


#Suma de dos numeros enteros
suma = (23 + 46)
#Impresion de la suma de los numeros enteros mas un string que dice Suma:
print("Suma: 23 + 46 =", (suma))
##Imprime el tipo de dato del resultado, que es 'int'.
print("Suma: 23 + 46 =",type(suma))


