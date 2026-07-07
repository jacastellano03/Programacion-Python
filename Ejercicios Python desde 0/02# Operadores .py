# Operadores

'''
Los operadores en Python son esenciales para realizar todo tipo de calculos y comparaciones.
Los operadores nos permiten realizar operaciones matematicas, comparar valores, y evaluar
expresiones logicas, entre otras cosas.

'''




"""
Los operadores aritmeticos son los operadores basicos como:

SUMA--[+]
RESTA--[-]
MULTIPLICACION--[*]
DIVISION--[/]
MODULO--[%]
EXPONENTE--[**]
DIVISION ENTERA--[//]

"""
print("OPERADORES ARITMETICOS")

print(f"Suma: 10 + 3 = {10+3}")
print(f"Resta: 10 - 3 = {10-3}")
print(f"Multiplicacion: 10 * 3 = {10*3}")
print(f"Division: 10 / 3 = {10/3}")
print(f"Modulo: 10 % 3 = {10%3}")
print(f"Exponente: 10 ** 3 = {10**3}")
print(f"Division entera: 10 // 3 = {10//3}")

print(15+13)            #SUMA
print(27-14)            #RESTA
print(7*7)              #MULTIPLICAION
print(12/3)             #DIVISION
print(10%2)             #MODULO
print(3**2)             #EXPONENTE
print(300//5)           #DIVISION ENTERO

print("just example of combinations")
print(3**2+5-9*4/3 //4)
print("Hola " * 5)
print("Hola " * (2**3))             # 8 veces hola

my_float= 2.5 * 2
print("Hola " * int(my_float))

print("HOLA " + "Python "+ "Que tal?")
print("Hola " + str(5))


"""
Operadores de comparacion son:

IGUALDAD[==]
DESIGUALDAD[!=]
MAYOR QUE--[>]
MENOR QUE--[<]
MAYOR O IGUAL QUE--[>=]
MENOR O IGUAL QUE--[<=]

"""
# Operadores de comparacion

print("OPERADORES DE COMPARACION")

print(f"Igualdad: 52 == 53 es {52 == 53}")
print(f"Desigualdad: 47 != 50 es {47 != 50}")
print(f"Mayor que: 70 > 30 es {70 > 30}")
print(f"Menor que: 70 > 30 es {70 < 30}")
print(f"Mayor o igual que: 33 >= 33 es {33 >= 33}")
print(f"Menor o igual que: 750 <= 700 es {750 <= 700}")

print('Just examples')
print(3 > 4)            # MAYOR QUE--[>] 
print(3 < 4)            # MENOR QUE--[<]
print(3 >= 4)           # MAYOR O IGUAL QUE--[>=]
print(3 <= 4)           # MENOR O IGUAL QUE--[<=]
print(3 == 4)           # IGUALDAD[==]
print(3 != 4)           # DESIGUALDAD[!=]

print("with cadenas de texto")
print("Hola">"Python")
print("Hola" == "Hola")
print("Hola" != "Python") 
print("Hola" >= "Bola")
print("Hola" >= "Zola")
print("aaaa" >= "aaaa")
print("aaaa" >= "abaa")     # Compara en ordanacion alfabetica cual es mayor
print("AAAA" >= "aaaa")
print("aaaa" >= "AAAA")

print(len("aaaa") >= len("abaa"))     # Sirve para saber cuántos elementos hay en total en una estructura.

"""
Condicionales

if    --> Se utiliza para ejecutar una acción solo cuando una condición es verdadera.

elif  --> Se utiliza para evaluar otra condición cuando la condición anterior no se cumple.

while --> Se utiliza para repetir instrucciones mientras una condición sea verdadera.

Operadores logicos son:

AND [&&] --> Se cumple o es verdadera cuando ambas afirmaciones son verdaderas
OR [||]  --> Se cumple si ambas o solo una afirmacion es verdadera
NOT--[!] --> En esta no se debe andar combinando nada

Ejemplo: print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
         print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}")
         print(f"NOT !: 10 + 3 == 14 es {10 + 3 == 14}")
"""

# Operadores de logicos

print("OPERADORES LOGICOS")

print(f"AND&&: 50 - 30 == 20 and 900 + 100 == 1000 es {50 - 30 == 20 and 900 + 100 == 1000}") # Se cumple ya que ambas son verdaderas
print(f"AND&&: 270 + 330 == 500 and 700 - 200 == 500 es {270 + 330 == 500 and 700 - 200 == 500}") # No se cumple porque una es Falsa (Ambas deben ser verdaderas en el AND)

print(f"OR||: 50 - 30 == 20 and 900 + 100 == 1000 es {50 - 30 == 20 and 900 + 100 == 1000}") # En el OR se cumple porque ambas son verdaderas
print(f"OR||: 75 + 45 == 120 or 400 - 500 == 0 es {75 + 45 == 120 or 400 - 500 == 0}") # Se cumple tambien por que una es verdadera (Una debe ser verdadera para sea True)
print(f"OR||: 600 - 300 = 900 or 50 + 10 == 70 es {600 - 300 == 900 or 50 + 10 == 70}") # No se cumple por que ninguna es verdadera

print(f"NOT!: 475 + 25 == 501 es {475 + 25 == 501} ") # Es falso porque la afirmacion esta incorrecta
print(f"NOT!: not 475 + 25 == 501 es {not 475 +25 == 501}") # Es verdadera porque estamos poniendo el not es decir estamos condicionando la afirmacion

print(3 < 4 and "Hola"<"Python")            #Se cumple o es verdadera cuando ambas afirmaciones son verdaderas
print(3 > 4 and "Hola">"Python")
print(3 > 4 or "Hola"<"Python")             #Se cumple si ambas o solo una afirmacion es verdadera
print(3 > 4 or "Hola">"Python")

print(3 > 4 or "Hola">"Python"and 4 == 4)
print(3 < 4 or "Hola">"Python"and 4 == 4)

print(not (3 > 4))
print(3 > 4)

print("EJERCICIOS")

print("Exercise 1")
#1. Realiza las siguientes operaciones aritméticas:
    #Suma: 15 + 25
    #Resta: 50 - 22
    #Multiplicación: 8 * 7
    #División: 100 / 20

print("Suma: 15 + 25 =",(15+25))
print("Resta: 50 - 22 =", (50-22))
print("Multiplicación: 8 * 7 =", (8*7))
print("División: 100 / 20 =", (100/20))


print("Exercise 2")
# 2. Calcula el resto de la división de 37 entre 5 y almacénalo en una variable remainder. Luego imprímelo.

remainder = (37 / 5)
print("remainder=",remainder)


print("Exercise 3")
# 3. Convierte el número 7 en una cadena de texto y concaténalo con la frase “ es mi número favorito”.Imprime el resultado.

my_number=7
print(my_number)

my_number_to_my_new_str_number = str(my_number)
print(my_number_to_my_new_str_number)

print("es mi número favorito: ", my_number_to_my_new_str_number)


print("Exercise 4")
# 4. Repite la palabra “Python” 10 veces usando el operador de multiplicación para cadenas y luego imprímela.
print("Hola " * 5)
print("Hola " * (2**3))             # 8 veces hola

print("Python " * 10 )


print("Exercise 5")
# 5. Crea dos variables: a y b con los valores 12 y 8 respectivamente. Compara si a es mayor que b y almacena el resultado en una variable booleana resultado. Imprime el valor de resultado.

a = 12
b = 8

result = ( a > b)
print(result)


print("Exercise 6")
# 6. Compara dos cadenas de texto (“apple” y “banana”) usando los operadores > y < y explica cuál tiene mayor orden alfabético.

c = ("apple")
d = ("banana")

result = (c > d)
print(result)         

print("apple">"banana")
print("apple"<"banana")

print("apple">="banana")        # Banana es mayor que apple ya que alfabeticamente va primero banana
                                #Se utiliza el mayor igual para saber cual es mayor alfabeticamente


print("Exercise 7")
# 7. Realiza una comparación lógica usando and para verificarsi el número 10 es mayor que 5 y menor que 20. Imprime el resultado.

a= 10
b= 5
c= 20

result3 = (a > b and a < c)
print(result3)

result2 = (10 > 5 and 10 < 20)
print(result2)


print("Exercise 8")
# 8. Usa el operador or para verificar si el número 7 es menor que 3 o mayor que 5. Imprime el resultado.

x = 7
y = 3
z = 5

result4 = (x < y or x > z)
print(result4)

result5 = (7 < 3 or 7 > 5)
print(result5)


print("Exercise 9")
# 9.  Aplica el operador not para invertir el resultado de la comparación 15 > 20. ¿Cuál es el resultado?

print(not( 15 > 20 ))

print(not(200 < 300))

print(not(175 < 100))

print(not(500 > 420))

print("Exercise 10")
# 10. Combina operadores aritméticos y lógicos: Verifica si el número resultante de la expresión (5 * 3) + 2 es mayor que 10 y menor que 20. Imprime el resultado.

result123 = ((5 * 3) + 2) > 10 and ((5 * 3) + 2 < 20)
print(result123)

resul = ((14 * 2) + 2) > 29 and ((15 * 2) - 5 > 30)
print(resul)


print(not(5==5))

print("Python" > "Java")

print(10%3+4)
print(5**2)

