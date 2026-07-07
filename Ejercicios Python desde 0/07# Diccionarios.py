### Diccionarios ###

'''
Los diccionarios son colecciones que almacenan pares de clave-valor, permitiendo
acceder a los valores de manera rapida mediante su clave. Esto hace que los 
diccionarios sean perfectos para representar datos estructurados, como las entradas
de una base de datos o la configuracion de una aplicacion.

'''

                                                    # Funciona como una estructura para organizar datos
my_dict = dict()
my_other_dict = {}
                                                    # Aqui en los diccionarios pondremos una claver y un valor es deicr funciona como: (Nombre:)(Alejandro)
print(type(my_dict))
print(type(my_other_dict))
                                                    # Un diccionario es un tipo de estructura en el que podemos almacenar datos de tipo "Clave -> Valor" 

my_other_dict = {"Nombre":"Alejandro", "Apellido":"Castellano", "Edad": 22}

my_dict = {
    "Nombre":"Alejandro", 
    "Apellido":"Castellano", 
    "Edad": 22,
    "Lenguajes":{"Paython","Swift","JavaScript"},               # Podemos tener dentro de un diccionario diferentes tipos de elementos ya sea diccionarios mismo o sets, tuplas, listas.
    1:1.69
    }

print(my_other_dict)

print(my_dict)
print(len(my_dict))                                 # Tiene solo 5 elementos ya que aqui solo se contabiliza el numero de claves que tenemos es decir 5

print(my_dict["Lenguajes"])                         # De esta manera accedemos a una clave de nuestro diccionario y nos termina devolviendo sus valores 
print(my_dict["Nombre"])                            # Para acceder a un elemento


my_dict["Edad"] = 25                                # Para actualizar una clave  
print(my_dict["Edad"])

my_dict["Apellido"] = "Jacome"
print(my_dict["Apellido"])



my_dict["Dirección"] = "7 de Agosto & Rodrigo Iturralde"            # Para agregar un nuevo campo a nuestro diccionario
print(my_dict)

my_dict["C.I."] = "0504147208"
print(my_dict)


del my_dict["Dirección"]                                            # Para eliminar datos eliminamos por clave
print(my_dict)


print("Alejandro" in my_dict)                                       # Tambien busca por clave
print("Jacome" in my_dict)                                          # Se usa el in para buscar si algo esta en nuestro diccionario pero este lo busca por clave
print("Edad" in my_dict)


print(my_dict.items())                          # Este (items) imprime los todos los datos dentro del diccionario tanto claves como valores.

print(my_dict.keys())                           # Este (keys) imprime todas las claves de nuestro diccinario

print(my_dict.values())                         # Este (values) imprime todos los valores que se encuentran dentro de las claves de nuestro diccionario



my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))              # Lo que hace esto es crear un diccionario sin valores
print(my_new_dict)

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_list, "Yoelinton")
print(my_new_dict)


print(list(my_new_dict))

print(tuple(my_new_dict))

print(set(my_new_dict))


#EXCERCICES.PY07``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
print("EJERCICIOS")


print("Exercise 1")
# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.

my_dict1 = {"name":"Alejandro", 
            "age":22, 
            "country":"Ecuador"
            }
print(my_dict1)



print("Exercise 2")
# 2. Accede al valor de la clave name en el diccionario.

print(my_dict1["name"])



print("Exercise 3")
# 3. Añade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.

my_dict1["Job"] = "Programdor"
print(my_dict1)



print("Exercise 4")
# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.

my_dict1["age"] = 38
print(my_dict1)



print("Exercise 5")
# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.

del my_dict1["country"]                     # En el diccionario se elimina valores por clave
print(my_dict1)



print("Exercise 6")
# 6. Crea un diccionario donde las claves sean números del 1al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).

my_dict6 = {1:1, 2:4, 3:9, 4:16, 5:25}
print(my_dict6)

squares = {x:x**2 for x in range(1, 6)}
print(squares)



print("Exercise 7")
# 7. Verifica si la clave age está presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.

my_dict7 = {"name": "Brais", "age": 37, "country": "Galicia"}
print("age" in my_dict7)

print("surname" in my_dict7)

my_dict7.items()
print(my_dict7)


print("Exercise 8")
# 8. Imprime solo las claves del diccionario.

print(my_dict1.keys())
print(my_dict6.keys())
print(my_dict7.keys())



print("Exercise 9")
#9. Convierte las claves del diccionario en una lista e imprime la lista resultante.

print(list(my_dict1))
print(list(my_dict6))                       # Forma 1
print(list(my_dict7))


my_list9 = my_dict1.keys()
print(list(my_list9))

my_list91 = my_dict6.keys()                 # Forma 2
print(list(my_list91))

my_list92 = my_dict7.keys()
print(list(my_list92))



print("Exercise 10")
# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".

my_list10 = ["name", "age", "job"]                                                                      # Creamos una lista

my_dict10 = dict.fromkeys(my_list10)                                                                    # Convertimos nuestra lista en un diccionario y la asociamos con el fromkeys() 

my_dict10 = dict.fromkeys(my_list10, "Desconocido")                                                     # Usamos el fromkeys para asignar un valor a todas las claves de nuestro diccionario.
print(my_dict10)



mylist1 = ['name', 'age', 'Job']

my_dict11 = dict.fromkeys(mylist1, "Bad Bunny")
print(my_dict11)


mylis2 = [1, 2, 3, 4, 5]

my_dict12 = dict.fromkeys(mylis2, "Alfredo33")
print(my_dict12)

mylist3 = ['name', 'age', 'country']

my_dict13 = dict.fromkeys(mylist3, "Yoelinton KIUU")
print(my_dict13)

# Un diccionario es una estructura de datos que almacena pares clave-valor

