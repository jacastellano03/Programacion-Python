students_list = [ "Ana",
    "Luis",
    "Carlos",
    "María",
    "Sofía",
    "Daniel",
    "Valentina",
    "Jorge",
    "Camila",
    "Mateo"]

# las funciones normalmente describen acciones por lo tanto aqui pondremos show_students
def show_students():                     #Cuando definimos una funcion esta debe ser distinta de nuestra lista y conjunto de datos que vayas a utilizar
    for element in students_list:
        print(element)
        
#student_list()                   # La funcion no se imprime si no la llamamos y asi es como se llama...


#print(students_list[0])

#print(students_list[7])

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