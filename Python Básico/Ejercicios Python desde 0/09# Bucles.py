### Bucles ###

'''
Los bucles nos permiten repetir bloques de codigo de forma eficiente evitando la 
necesidad de escribir el mismo codigo una y ota vez. En Python , los bluces son 
escensiales para trabajar con colecciones de datos y ejecutar tareas repetitivas 
de manera rapida y limpia.
Uso del --> (While y For)

While-->Este tipo de bucle ejecuta un bloque de código mientras una condición sea verdadera.
        Es ideal cuando no sabemos exactamente cuántas veces se debe repetir el ciclo, pero tenemos 
        una condición que debe cumplirse para continuar la ejecución.

For --> Este tipo de bucle se utiliza principalmente para iterar sobre colecciones de datos,
        como listas, tuplas, sets y diccionarios. Es perfecto para recorrer cada elemento de una 
        colección de forma ordenada.

'''
# while
print('My condition 0')
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1


print('My condition 1')
my_conditionn = 0

while my_conditionn < 10:
    print(my_conditionn)
    my_conditionn += 2
else: #Es opcional                                        # Solo podemos usar el else con el while ya que se considera casi como un if
    print('Mi condicion es mayor igual que 10')

print('La ejecucion continua')

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print('Mi condicion es 15')

    print(my_condition)

print('La ejecucion continua')


print('My condition 1')
my_condition1 = 0

while my_condition1 < 20:
    print(my_condition1)
    my_condition1 += 1
    if my_condition1 == 15:
        print('Se detiene la ejecucion')
        break
print('La ejecucion continua')


# for
print('FOR')                                    # Hace que se repitan los elementos de un conjunto de datos

my_list = [22, 10, 30, 29, 40, 26, 10]                                      #Guardan elementos de 1 en 1 de forma ordenada

for element in my_list:
    print(element)


my_tuple = (22, 1.70, "Alejandro", "Castellano", "Alejandro")               #Guardaban elemntos q nos se pueden retocar

for element in my_tuple:
    print(element)

my_set = {"Alejandro", "Castellano", 22}                                    #Guardaban elementos q no se pueden repetir

for element in my_set:
    print(element)

my_dict = {"Nombre":"Alejandro", "Apellido":"Castellano", "Edad": 22, 1:"Python"}         #Guardaban elementos de clave valor

for element in my_dict:
    print(element)
    if element == "Apellido":
        break
    print('Se ejecuta')
else:               #Este else nose muestra pq hemos roto el bucle con el break
    print('El bucle for para mi diccionario ha finalizado')


print("Ejemplo con continueeeee")
my_dict2 = {"Nombre":"Alejandro", "Apellido":"Castellano", "Edad": 22, 1:"Python"}         #Guardaban elementos de clave valor

for element in my_dict2:
    print(element)
    if element == "Edad":
        continue                    #Es como una especie de break que rompe el codigo en punto y luego lo empieza desde el inicio es decir desde for
    print('Se ejecuta')

else:             
    print('El bucle for para mi diccionario ha finalizado')



#EXCERCICES.PY09``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

print("EJERCICIOS")


print("Exercise 1")
# 1. Usa un bucle while para imprimir los números del 1 al 10.

my_condition1 = 1

while my_condition1 <= 10:
    print(my_condition1)
    my_condition1 += 1



print("Exercise 2")
# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada número.

mylist2 = [10, 20, 30, 40, 50]

for element in mylist2:
    print(element)



print("Exercise 3")
# 3. Escribe un programa que use un bucle while para sumar los números del 1 al 100 e imprime el resultado.

numero = 1
suma = 0
while numero <= 100:
    suma += numero
    numero += 1
print("La suma es:", suma)

# Escribe un programa que use un bucle while para sumar los números del 1 al 50 e imprime el resultado.

suma = 0
numero = 1

while numero <= 50:
    suma += numero
    numero += 1
print("La suma es:", suma)


# Escribe un programa que use un bucle while para imprimir todos los números pares del 1 al 100.

numero = 1

while numero <= 100:
    if numero %2 == 0:                  # Para decir que un numero es divisible para dos
        print(numero)
    numero +=1


# Escribe un programa que use un bucle while para mostrar una cuenta regresiva desde 20 hasta 1.

numero = 20

while numero >= 1:
    print(numero)
    numero -=1

# Escribe un programa que use un bucle while para mostrar la tabla de multiplicar del 7 (del 1 al 10).

contador = 1

while contador <= 10:
    print("7 x", contador, "=", 7 * contador)
    contador +=1



print("Exercise 4")
#4. Escribe un bucle for que imprima cada carácter de la cadena “Python”.

word = "Python"

for element in word:
    print(element)

# Escribe un programa que use un bucle for para contar cuántas letras tiene la palabra "Universidad" y muestre el total.
# Contar letras de "Universidad"

word1 = "Universidad"

for element in word1:
    print(element)

# Escribe un programa que use un bucle for para imprimir cada carácter de la palabra "Programación".
# Imprimir caracteres de "Programación"

word2 = "Programación"

for element in word2:
    print(element)


# Escribe un programa que use un bucle for para contar cuántas vocales tiene la palabra "Administración".
# Contar vocales en "Administración"

word3 = "Administración"
contador = 0

for letter in word3:
    if letter.lower() in "aeiou":
        contador +=1

print("Numero de vocales:", contador)

# Escribe un programa que use un bucle for para imprimir la palabra "Hola" 5 veces.
# Imprimir "Hola" 5 veces

for i in range (5):
    print("WestCOL")


# Escribe un programa que use un bucle for para imprimir cada carácter de la palabra "ingeniería" en mayúsculas.
# Imprimir "ingeniería" en mayúsculas letra por letra

word4 = "ingeniería"

for letter in word4:
    print(letter.upper())


# Escribe un programa que use un bucle for para imprimir la palabra "Código" al revés.
# Imprimir "Código" al revés

word5 = "Código"

for letter in word5[::-1]:
    print(letter)



print("Exercise 5")
# 5. Usa un bucle while para encontrar el primer número divisible por 7 entre 1 y 50.

number = 1

while number <= 50:
    if number % 7 == 0:
        print(number)
        break
    number += 1



print("Exercise 6")
# 6. Usa un bucle for para recorrer el diccionario {“name”: “Brais”, “age”: 37, “country”: “Galicia”} e imprime las claves.

my_dict1 = {'name': 'Brais', 'age': 37, 'country': 'Galicia'}

for key in my_dict1:
    print(key)



print("Exercise 7")
# 7. Escribe un programa que use un bucle while para imprimir los números pares entre 1 y 20.

l = 1

while l <= 20:
    if l %2 == 0:
        print(l)
    l += 1                  #Este es muy importante ya que hace que se imprima el codigo



print("Exercise 8")
#8. Usa un bucle for con la función range() para imprimir los números del 1 al 10 en orden inverso. 

for l in range(10, 0, -1):          #Para imprimir numero en orden inverso
    print(l)    
    


print("Exercise 9")
# 9. Escribe un programa que use un bucle for para contar cuántas veces aparece el número 30 en la lista[30, 10, 30, 20, 30, 40].

mylist1 = [30, 10, 30, 20, 30, 40]
print(mylist1.count(30))
counter = 0

for element in mylist1:
    if element == 30:
        counter +=1
print(counter)



print("Exercise 10")
# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre “Brais”.

names = ["Sara", "Brais", "Pedro"]

for element in names:
    print(element)
    if element == "Brais":
        break
print('Se encontro a Brais')


for i in range(3):
    print(i)


for i in range (10):
    print('WestCOL')