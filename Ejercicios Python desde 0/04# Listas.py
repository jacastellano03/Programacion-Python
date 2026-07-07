###Listas###

"""
En Python las listas son colecciones ordenadas de elementos que pueden almacenar
diferentes tipos de datos, y permiten realizar una gran variedad de operaciones
desde la manipulacion de sus elementos hasta la creacion de sublistas.

"""

# Formas de crear listas

"""
my_list = list()                                            # Su constructor simple
my_list - []

"""

"""
lista.append(34) # agregar elementos
print(lista)
lista.remove(2) # eliminar elementos
print(lista)
lista[1] = 22 # cambiar valor de un indice, en este caso el 1
print(lista)
lista.sort() # ordenar de menor a mayor valor
print(lista)

"""
                                                                            # para saber cuántas veces aparece un elemento específico se usa count()
                                                                            # para saber cuántos elementos hay en total en una estructurase usa len()
print("Listas")

my_list = list()                                # Una lista es como una caja en la cual vamos agregando elementos cada uno en una diferente posicion 0,1,2,3 etc
print(len(my_list))
                                                #Empiezan las listas con cada dato ordenado desde el elemento 0.1.2.3.4 etc
my_other_list = []

#Lista de edades,
my_list = [22, 10, 26, 30, 29, 40, 26, 10, 10]
print(type(my_list))
print(my_list)
print(len(my_list))                             # Para saber cuantas veces tenemos un valor especifico de elementos en nuestra lista

# print(my_list.index("Alejandro")) IndexError 'Alejandro' is not in list

print("Tenemos", my_list.count(26), "veces el 26.")               # Sirve para saber cuántas veces aparece un elemento específico.
print(my_list.count(40))
print(my_list.count(10))



                 #0   #1       #2         #3
my_other_list = [22, 1.69, "Alejandro", "Caste"]
print(type(my_other_list))
print(my_other_list)

print(my_other_list[0])                         # Para acceder a los elementos de nuestra lista
print(my_other_list[1])
print(my_other_list[-1])                        # Toma el ultimo elemento de nuestra lista
print(my_other_list[-4])
#print(my_other_list[-5])                       #  Error ya que solo tenemos hasta el elemento -4

print('kkkkkk')
print(my_other_list.index("Alejandro"))


age, height, name, surname = my_other_list
print(name)
print(height)

age, height, address, surname = my_other_list
print(address)                                  # Nos va a imprimir de igual forma el name

name, height, age, surname = my_other_list[2],my_other_list[1],my_other_list[0],my_other_list[3]
print(age)
print(name)


print(my_list + my_other_list)
#print(my_list - my_other_list)                 #error


#Paython es de tipado dinamico

my_list = "Hola Python"
print(my_list)
print(type(my_list))

my_list = list("Hola Python")
print(my_list)
print(type(my_list))


#Para empezar a trabajar con los elementos de la lista utilizamos esto 

print("Mi lista")
my_other_list = [1.69, "Alejandro", 22, "Caste", 22]
my_other_list.append("Jacome")                                  # Para agregar elementos
print(my_other_list)

my_other_list.insert(1, "Rojo")                                # El insert se usa para agregar elementos en la posicion en que nosotros queramos
print(my_other_list)

my_other_list[1] = "Verde"                                     # Se utiliza para cambiar o actualizar una variable
print(my_other_list)

my_other_list.insert(0, "Jhoel")
print(my_other_list)

my_other_list.remove(22)                                        #Elimina el primer valor que encuentra teniamos 2 veces el 22 y solo elimino el primero
print(my_other_list)

my_other_list.remove("Jhoel")                                   #El remove se usa para eliminar elementos que conocemos que estan dentro de nuestra lista
print(my_other_list)

my_list = [22, 10, 26, 30, 29, 40, 26, 10, 17]

print(my_list.pop())                                            #Se utiliza para eliminar un elemento pero que queremos saber que elemento eliminamos ya que lo imprime
print(my_list)


print(my_list.pop(3))                                           # Elimina el numero 30 ya que es la variable que esta en la posicion numero 3
print(my_list)

print("para eliminar elementos con los que ya no queremos trabajr")
my_list = [22, 10, 26, 30, 29, 40, 26, 10, 17]
print(my_list)

del my_list[1]                                                  #Se usa del para eliminar una variable por indice 
print(my_list)

del my_list[0]
print(my_list)

my_new_list = my_list.copy()                                #Sirve para copiar una lista en algun punto y luego imprimirla cuando queramos

my_list.clear()                                           # Este se usa para eliminar todos los elemntos q estan dentro de nuestra lista
print(my_list)

print(my_new_list)

my_new_list.reverse()                                       #Para darle la vuelta a la lista que tenemos
print(my_new_list)

my_new_list.sort()                                          #Sirve para ordanar la lista en su defecto ya sea en orden numerico u alfabetico
print(my_new_list)


print(len(my_other_list))                                       # Para saber cuantos elementos tenemos en nuestra lista

print("Tenemos", my_other_list.count(1.69), "veces la edad.")               # Retorna el numero de ocurrencias de un valor es decir cuenta cuantas variables de las misma tenemos en nuestra lista


#EXCERCICES.PY04``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
print("EJERCICIOS")

print("Exercise 1")
# 1. Crea una lista con los números del 1 al 5 e imprímela.

my_list23 = list[1, 2, 3, 4, 5]
print(my_list23)

my_list1 = [1, 2, 3, 4, 5]                          #Es mejor hacer la lista d esta forma usando los corchetes
print(my_list1)


print("Exercise 2")
#2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].

my_list2 = [10, 20, 30, 40, 50]
print(my_list2[3])                                  #El tercer elemento de la lista dio como resultado 40
print(my_list2[0])

my_list2 = [22, 10, 26, 30, 29, 40, 26, 10, 17]
print(my_list2[5])                                  #Accedimos al 5to elemento de la lista


print("Exercise 3")
# 3. Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] e imprímela.

my_list3 = [1, 2, 3, 4, 5]
print(my_list3)

print(my_list3.index(3))

my_list3.append(6)
print(my_list3)

# Agrega el número 100 al final de la lista [20, 40, 60, 80].

my_list3 = [20, 40, 60, 80]
print(my_list3)

my_list3.append(100)
print(my_list3) 

# Inserta el número 15 en la posición 1 de la lista [10, 20, 30, 40].

my_list3 = [10, 20, 30, 40]
print(my_list3)

my_list3.insert(1, 15)
print(my_list3)
# Muestra cuántos elementos tiene la lista [5, 10, 15, 20, 25].

my_list3 = [5, 10, 15, 20, 25]
print(len(my_list3))

# Dada la lista [10, 20, 30], agrega el número 40 al final.

my_list3 = [10, 20, 30]
print(my_list3)

my_list3.append(40)
print(my_list3)


print("Exercise 4")
# 4. Inserta el número 15 en la posición 2 de la lista [10, 20, 30, 40, 50].

my_list4 = [10, 20, 30, 40, 50]
print(my_list4)

my_list4.insert(2, 15)
print(my_list4)

# Inserta la palabra "hola" en la posición 2 de la lista ["a", "b", "c", "d"].

my_list4 = ["a", "b", "c", "d"]
print(my_list4)

my_list4.insert(2, "hola")
print(my_list4)

# Inserta el número 55 en la posición 3 de la lista [11, 22, 33, 44, 66].

my_list4 = [11, 22, 33, 44, 66]
print(my_list4)

my_list4.insert(3, 55)
print(my_list4)

# Inserta tu nombre en la posición 0 de la lista ["Juan", "Pedro", "Luis"].

my_list4 = ["Juan", "Pedro", "Luis"]
print(my_list4)

my_list4.insert(0, "Alejandro")
print(my_list4)


print("Exercise 5")
# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].

my_list50 = [10, 20, 30, 30, 40, 50]              
print(my_list50)

my_list51 = [10, 20, 30, 30, 40, 50]              
print(my_list50)

#forma 1
my_list50.remove(30)                                     # Elimina el primer valor que encuentra teniamos 2 veces el 22 y solo elimino el primero
print(my_list50)                                         # El remove se usa para eliminar elementos que conocemos que estan dentro de nuestra lista

#forma 2
del my_list51[2]                                         # Se usa del para eliminar una variable por indice
print(my_list51)


print("Exercise 6")
# 6. Usa la función pop() para eliminar el último elemento de la lista [1, 2, 3, 4, 5] y almacénalo en una variable. Imprime la variable y la lista.

my_list6 = [1, 2, 3, 4, 5]
print(my_list6)


my_last_element = my_list6.pop()
print(my_last_element)
print(my_list6)

# Usa pop() para eliminar el último elemento de la lista [10, 20, 30, 40]. Guárdalo en una variable e imprime la variable y la lista.

my_list6 = [10, 20, 30, 40]
print(my_list6)

last_element = my_list6.pop()
print(last_element)

print(my_list6)

# Usa pop() para quitar el último color de la lista ["rojo", "azul", "verde"].

colors = ["rojo", "azul", "amarisho", "verde"]
print(colors)

last_color = colors.pop()
print(last_color)

print(colors)

# Dada la lista ["a", "b", "c", "d"], elimina el último valor usando pop() y muéstralo.

abecedario = ["a", "b", "c", "d"]
print(abecedario)

last_word = abecedario.pop()
print(last_word)

print(abecedario)

# Dada la lista ["lunes", "martes", "miércoles", "jueves"], elimina el último día con pop().

days = ["lunes", "martes", "miércoles", "jueves", "viernes"]
print(days)

last_day = days.pop()
print(last_day)

print(days)


print("Exercise 7")
# 7. Invierte la lista [100, 200, 300, 400, 500] e imprímela.

my_list7 = [100, 200, 300, 400, 500]
print(my_list7)

my_list7.reverse()
print(my_list7)


days = ["lunes", "martes", "miércoles", "jueves", "viernes"]
print(days)

days.reverse()
print(days)


abecedario = ["a", "b", "c", "d"]
print(abecedario)

abecedario.reverse()
print(abecedario)


print("Exercise 8")
# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprímela.

my_list8 = [3, 1, 4, 2, 5]
print(my_list8)

my_list8.sort()
print(my_list8)

my_list81 = [22, 10, 26, 30, 29, 40, 26, 10, 17]
print(my_list81)

my_list81.sort()
print(my_list81)


print("Exercise 9")
# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.

my_list9_1 = [1, 2, 3]
print(my_list9_1)

my_list9_2 = [4, 5, 6]
print(my_list9_2)

my_new_list9 = my_list9_1 + my_list9_2
print(my_new_list9)

# Une ["lunes", "martes"] con ["miércoles", "jueves", "viernes"].

my_list9_3 = ["lunes", "martes"]
print(my_list9_3)

my_list9_4 = ["miércoles", "jueves", "viernes"]
print(my_list9_4)

my_new_list9_9 = my_list9_3 + my_list9_4
print(my_new_list9_9)

# Concatena [11, 22, 33] con [44, 55].

cadena1 = [11, 22, 33]
print(cadena1)

cadena2 = [44, 55]
print(cadena2)

new_cadena = cadena1 + cadena2
print(new_cadena)

# Une las listas ["a", "b"] y ["c", "d", "e"].

list1 = ["a", "b"]
print(list1)

list2 = ["c", "d", "e"]
print(list2)

new_list = list1 + list2
print(new_list)


print("Exercise 10")
# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posición 1 hasta la 3 (sin incluir la posición 3).

my_list_10 = [10, 20, 30, 40, 50]
print(my_list_10)

sub_list = my_list_10[1:3]                                                      #Cuando colocamos la ultima posicion de nuestra variable esta no se incluye si queremos incluirla debemos poner una variable mas aparte del numero que es decir una posicion mas 
print(sub_list)

# Obtén una sublista de ["a", "b", "c", "d", "e"] desde la posición 1 hasta la 3.

my_list_10 = ["a", "b", "c", "d", "e"]
print(my_list_10)

sub_list = my_list_10[1:4]                                                      #Colocamos hasta el 4 ya que no esta excluyendo el numero 3 entonces si quiere este incluida en la sublista
print(sub_list)

# Crea una sublista con los elementos de [1, 2, 3, 4, 5] desde la posición 0 hasta la 2.

my_list_10 = [1, 2, 3, 4, 5]
print(my_list_10)

sub_list = my_list_10[0:3]                          
print(sub_list)


             #0  #1   #2  #3  #4
my_list_10 = [1,  2,  3,  4,  5]                    # Cuando imprimimos una sublista de esta forma, se imprime desde la variable 0 es decir como colocamos [1:4] se imprimira del 2 al numero 4 la sublista
print(my_list_10)

print(my_list_10[1:4])
