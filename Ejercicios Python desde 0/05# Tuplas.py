### Tuplas ###

'''
Las tuplas en Python son una estructura de datos similar a las listas, pero con una
diferencia clave: las tuplas son inmutables, lo que significa que, una vez creadas,
no pueden modificarse. Esta caracteristica las hace ideales para almacenar datos que
no deben cambiar a lo largo de la ejecucion del programa, aportando mas seguridad en
ciertos contextos
 
'''
print("TUPLAS")


my_tuple = tuple()                                          # Su constructor simple
my_other_tuple = ()

my_tuple = (22, 1.70, "Alejandro", "Castellano", "Alejandro")
my_other_tuple = (35, 60, 30)



print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])                      #Tambien podemos acceder normalmente a los elemntos de la tupla como lo hicimos en la lista empezando desde cero cada variable
print(my_tuple[-1])
#print(my_tuple[4])     IndexError
#print(my_tuple[-1])    IndexError      #Ambos son errores ya que esos valores no tenemos en la tuple

print(my_tuple.count("Alejandro"))              # Usamos el count para contar cuantas veces aperce en nuestra tupla

print(my_tuple.count("Jacome"))                 # Nos da como cero ya que esta variable no existe en nuestra tupla


print(my_tuple.index("Castellano"))             # Se usa para saber en pocision se encuentra nuestra variable o para saber cual es el indice de la variable

print(my_tuple.index("Alejandro"))


# my_tuple[1] = 1.80     'tuple' object does not support item assignment         # No se puede modificar las tuplas a menos que las transformemos a listas y luego y las regresemos a tuplas
# print(my_tuple)

my_sum_tuple = (my_tuple + my_other_tuple)                  # Las tuplas por deficion no son mutables osea que se les puede modificar
print(my_sum_tuple)

print(my_sum_tuple[2:4])                                    # Tambien podemos tomar elementos de las tuplas de una variable especifica que queramos a otra


print("Para modificar tuplas lo hacemos asi ->")

my_tuple = list(my_tuple)                       # Para agregar elementos a nuestra tupla debemos cambiarla a lista
print(type(my_tuple))

my_tuple[4] = "JACOME"                          # Aqui sucedio la magia agregamos un elemento a nuestra tupla
print(my_tuple)

my_tuple = tuple(my_tuple)                      # Es necesario regresar nuestra lista a tupla como estaba originalmente 
print(my_tuple)

print(type(my_tuple))


### CONCEPTOS ###

# TUPLA -> Inmutable

# LISTA  -> Mutable

#del my_tuple [2]            NameError: name 'my_tuple' is not defined

del my_tuple

# print(my_tuple)           NameError: name 'my_tuple' is not defined

#EXCERCICES.PY05``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
print("EJERCICIOS")


print("Exercise 1")
# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprímela.

my_tuple1 = (10, 20, 30, 40, 50)
print("Mi tupla 1:", my_tuple1)



print("Exercise 2")
# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.

my_tupla2 = (100, 200, 300, 400, 500)
print("Mi tupla 2:", my_tupla2)

print(my_tupla2[2])



print("Exercise 3")
# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.

my_tupla3 = (1, 2, 3)

my_tupla3 = list(my_tupla3)                             # Cambiamos de tupla a lista
print(my_tupla3)
print(type(my_tupla3))

my_tupla3[0] = 10                                       # Aqui modificamos el el valor numero 1 en el 0 de la tupla original a 10

my_tupla3 = tuple(my_tupla3)                            # Regresamos el type de list a tuple
print(my_tupla3)
print(type(my_tupla3))


my_tupla31 = (100, 200, 300, 400, 500)

my_tupla31 = list(my_tupla31)                           # Cambiamos de tupla a lista
print(my_tupla31)
print(type(my_tupla31))

my_tupla31[2] = 10000                                   # Aqui modificamos el el valor numero 300 en el 2 de la tupla original a 10000

my_tupla31 = tuple(my_tupla31)                          # Regresamos el type de list a tuple
print(my_tupla31)
print(type(my_tupla31))



print("Exercise 4")
# 4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).

my_tuple4 = (1, 2, 3, 3, 4, 5, 3, 3)
print(my_tuple4)

print("El número 3 aparece:", my_tuple4.count(3),"veces.")

# Cuenta cuántas veces aparece el número 9 en la tupla (9, 8, 7, 9, 6, 9, 5)

my_tuple4 = (9, 8, 7, 9, 6, 9, 5)
print(my_tuple4)

print("El número 9 aparece:", my_tuple4.count(9),"veces.")

# Cuenta cuántas veces aparece el número 7 en la tupla (7, 7, 7, 2, 4, 6, 7)

my_tuple4 = (7, 7, 7, 2, 4, 6, 7)
print(my_tuple4)

print("El número 7 aparece:", my_tuple4.count(7),"veces.")



print("Exercise 5")
# 5. Encuentra el índice de la primera aparición de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").

my_tuple5 = ("Java", "Python", "JavaScript", "Python")
print(my_tuple5)

print(my_tuple5.index("Python"))                    #Para encontra el indice se usa index y se coloca la variable de la cual necesitamos saber cual numero de indice tiene



print("Exercise 6")
# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.

my_tupla61 = (1, 2, 3)
print("Tupla 1:",my_tupla61)
my_tupla62 = (4, 5, 6)
print("Tupla 2:",my_tupla62)

my_sum_tuple6 = my_tupla61 + my_tupla62
print("Tupla restante:",my_sum_tuple6)



print("Exercise 7")
# 7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).

my_tupla7 = (10, 20, 30, 40, 50)
print(my_tupla7)

# print(my_tupla7[2:4])

my_sub_tuple7 = my_tupla7[2:4]
print("Mi sub tupla es:", my_sub_tuple7)



print("Exercise 8")
# Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.

my_tupla8 = ("rojo", "verde", "azul")
print(my_tupla8)
print(type(my_tupla8))

my_tupla8 = list(my_tupla8)
print(my_tupla8)
print(type(my_tupla8))

my_tupla8[2] = "amarillo"

my_tupla8 = tuple(my_tupla8)
print(my_tupla8)
print(type(my_tupla8))



print("Exercise 9")
# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.

my_tupla9 = ("rojo", "verde", "azul", "amarillo", "violeta")
print(my_tupla9)

del my_tupla9
# print(my_tupla9)                    NameError: name 'my_tupla9' is not defined



print("Exercise 10")
# 10. Crea una tupla con un solo elemento (el número 100)e imprímela. Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento.

my_tuple10 =(100, )                     # Para crear tuplas de un solo elementos nada mas se coloca una coma y un espacio al final example --> my_tuple10 =(100, ) 
print(my_tuple10)
print(type(my_tuple10))