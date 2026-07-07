### Sets ###

'''
Los sets en Python son estructuras de datos ideales para almacenar elementos unicos
y realizar operaciones como la union, interseccion y diferencia. Los sets en Python
son colecciones no ordenadas y sin elementos duplicados, lo que los hace muy eficientes
cuando se trata de realizar busquedas y operaciones entre conjuntos de datos.

'''


print("SETS")                                       # No es una estructura ordenada por lo tanto no podemos acceder a un elemnto por su indice

my_set = set()                                      # Un set no es una estructura ordenada
print(type(my_set))

my_set = {}                                         # Su constructor simple

my_set = {"Alejandro", "Castellano", 22}            # Son estructuras buenisimas para guardar muchos datos pero no para buscar datos

my_set.add("Niño")                                  # Add se utiliza para agregar elementos
my_set.add("Yoelinton")
my_set.add("KLK")
my_set.add("ANUEL AA")

my_set.add("Niño")                                  # Un set no admite repetidos
my_set.add("Niño")
my_set.add("Niño")
print(my_set)

my_set.remove("Castellano")                         # remove se utiliza para eliminar elemntos de nuestro set
my_set.remove("KLK") 
my_set.remove("ANUEL AA") 

print(my_set)                                       # Para tener en cuenta un set cuando imprimos siempre cambia el orden de impresion


my_set.clear()                                      # clear se usa para eliminar todos los elementos que tenemos en nuestro set pero el set sigue creado pero vacio
print(my_set)
print(len(my_set))

# del my_set                                        # No se puede usar del en sets ya que aqui este nos termina eliminando nuestro set  
# print(my_set)                                     # NameError: name 'my_set' is not defined


my_other_set1 = {"Alejandro", "Castellano", "Jacome", 22}

my_list = list(my_other_set1)
print(my_list)

print(my_list[0])


my_other_set2 = {"Python", "Swift", "C++", "Kotlin"}


my_new_set = my_other_set1.union(my_other_set2)
print(my_new_set.union(my_new_set).union(my_other_set1).union({"JavaScript", "C#"}))           # Aqui estamos tratando de duplicar poniendo otra vez union de otros sets pero como son duplicados no se ponen solo se mantienen los que ya estaban
   
print(my_new_set.difference(my_other_set1))


print(my_new_set.intersection(my_other_set1))

print(my_new_set.intersection(my_other_set2))


print("Alejandro" in my_set)                        # Esta es la sintaxis para comprobar si un elemento esta en nuestro set
print("Niño" in my_set)
print("Jacome" in my_set)
print("Esponjita" in my_set)



#EXCERCICES.PY06``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
print("EJERCICIOS")


print("Exercise 1")
# 1. Crea un set con los números del 1 al 5 e imprímelo.

my_set1 = {1,2,3,4,5}
print(my_set1)
print(type(my_set1))



print("Exercise 2")
# 2. Añade el número 6 al set {1, 2, 3, 4, 5} e imprímelo.

my_set2 = {1, 2, 3, 4, 5}
print(my_set2)

my_set2.add(6)
print(my_set2)



print("Exercise 3")
# 3. Intenta añadir el número 5 al set {1, 2, 3, 4, 5} nuevamente. ¿Qué sucede?

my_set3 = {1, 2, 3, 4, 5}
print(my_set3)

my_set3.add(5)                          # No se puede añadir el 5 ya que es un elemnto que ya existe en nuestro y los sets no admiten repetidos
print(my_set3)



print("Exercise 4")
# 4. Verifica si el número 3 está en el set {1, 2, 3, 4, 5} e imprime el resultado.

my_set4 = {1, 2, 3, 4, 5}
print(my_set4)

print((3) in my_set4)
print((100) in my_set4)
print((1) in my_set4)



print("Exercise 5")
# 5. Elimina el número 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.

my_set5 = {1, 2, 3, 4, 5}
print(my_set5)

my_set5.remove(4)
print(my_set5)



print("Exercise 6")
# 6. Usa el método clear() para vaciar un set y luego imprime su longitud.

my_set6 = {1, 2, 3, 4, 5}
print(my_set6)

my_set6.clear()
print(my_set6)

print(len(my_set6))



print("Exercise 7")
# 7. Convierte el set {"manzana", "naranja", "plátano"} en una lista e imprime el primer elemento de la lista.

my_set7 = {"manzana", "naranja", "plátano"}

my_list7 = list(my_set7)

print(my_list7[0])                                  # Para imprimir elementos usamos los corchetes



print("Exercise 8")
# 8. Realiza la unión de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.

my_set81 = {1, 2, 3}
print("Set 1:", my_set81)

my_set82 = {4, 5, 6}
print("Set 2:", my_set82)

my_new_set8 = my_set81.union(my_set82)
print("Set new:",my_new_set8)



print("Exercise 9")
# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.

my_set91 = {1, 2, 3, 4}
print("Set 1:", my_set91)

my_set92 = {3, 4, 5, 6}
print("Set 2:", my_set92)


my_dif_set9 = my_set91.difference(my_set92)
print(my_dif_set9)



print("Exercise 10")
#10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.

my_set10 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(my_set10)

del my_set10              # No se puede usar del en sets ya que aqui este nos termina eliminando nuestro set 
# print(my_set10)         Index erros  NameError: name 'my_set10' is not defined.
