# Cadenas de texto

'''
Las cadenas de texto o strings son una de las estructuras de datos
mas importantes y utilizadas ya que nos permiten manipular y procesar
texto de diversas maneras. Python ofrece una gran cantidad de funciones
y metodos para manejar cadenas, lo que facilita su uso en aplicaciones
de todo tipo.

'''

#Strings

my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string))                       # Se utiliza para calcular el numero de caracteres de la variable
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de línea"        # Se utiliza el salto de linea tipeando \n
print(my_new_line_string)


my_tab_string = "Este es un string\tcon tabulación"        # Se utiliza el \t para dar un espacio de un tab en el texto 
print(my_tab_string)
my_tab_string = "\tEste es un string con tabulación"        
print(my_tab_string)


my_scape_string = "\tEste es un string\ncon escapado de linea"          #Se hizo una tabulacion y un salto de linea
print(my_scape_string)

my_scape_string = "\\tEste es un string\ncon escapado de linea"         #Solo se hizo el salto de linea por que otro se interfirio ya que se puso \\
print(my_scape_string)

#Formatear los strings
print("Formatear los strings")

"""
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"% - number of digitsf" - Floating point numbers with fixed precision

"""
name, surname, age = "Alejandro", "Castellano", 22

print("Mi nombre es %s %s y mi edad es %s".format(name,surname,age))
print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))        #Se usan estas formulas para que sea mas rapido la forma de trabajar

print("Mi nombre es %s %s y mi edad es %s" %(name,surname,age))
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))             #Se utiliza %d para los numeros enteros

print("Mi nombre es " + name + " " + surname + " y mi edad es" + str(age))  #No es una buena practica ya que nos demorariamos mas en hacer si trabajamos asi


#print("Mi nombre es {name} {surname} y mi edad es {age}")                  #Se debe colocar la f
print(f"Mi nombre es {name} {surname} y mi edad es {age}")                  #Esta es la forma mas rapida y util

#Desempaquetado de caracteres
print("Desempaquetado de caracteres")

lenguage= "Python"
a, b, c, d, e, f = lenguage                    #Se deben crear 6 variables para cada valor de la variable

print(a)
print(b)
print(c)
print(d)

# División
print("División")

#Texto de impresión: Python
lenguage_slice = lenguage[1:3]                  #Toma los letras exactas de nuestra variable
print(lenguage_slice)

lenguage_slice = lenguage[1:]                   #Pilla las letras desde donde empieza hasta el final
print(lenguage_slice)

lenguage_slice = lenguage[-2]                   #Es la o ya que empieza desde el final entonces n es -1 & o es -2
print(lenguage_slice)

# Reverse
print("Reverse")

#Texto de impresión: Python
reversed_lenguage = lenguage[::-1]              #Para imprimir el texto de atras para adelante
print(reversed_lenguage)

lenguage_slice = lenguage[1:2:5]
print(lenguage_slice)

lenguage_slice = lenguage[0:6:2]
print(lenguage_slice)


# Funciones del sistema para impresion del texto
print("Funciones")

#Texto de impresión: Python
print(lenguage.capitalize())                    #Se utiliza para poner la primera letra en mayuscula
print(lenguage.upper())                         #Se utiliza para poner toda la letra en mayuscula
print(lenguage.lower())                         #Para poner toda la variable en letras minusculas
print(lenguage.title())                         #Convierte la primera letra de cada palabra en mayúscula y las demás en minúscula.
print(lenguage.count("h"))                      #Sirve para saber cuántas veces aparece un elemento específico.
print("78".isnumeric())                         #Es como una variable booleana para confirmar un tipo txto 
print("LALA".isnumeric())
print(lenguage.upper().isupper())               #Se hizo una combinacion primero se coloco todas las letras en mayuscula y luego se metio una var booleana para confirmar si todas las letras son mayusculas therefore is true
print(lenguage.lower().isupper())               #Es falsa por que no cumple con el isupper
print(lenguage.startswith("Py"))                #Es verdadero a que la variable lenguage: Python si empieza asi
print(lenguage.startswith("py"))                #Es falso ya que no empieza con py sino con Py
print("Py" == "py")


print("EJERCICIOS")

print("Exercise 1")
# 1. Declara una variable text con la frase “Aprendiendo Python” y luego imprime la longitud de la cadena usando len().

text= "Aprendiendo Python"
print(len(text))

print("Exercise 2")
# 2. Concatena dos cadenas: “Hola” y “Python”, y muestra el resultado en una sola línea.

# Way number 1
print("Hola" + " " + "Python")

# Way number 2
a = "Hola"
b = "Python"

print(a + b)

a = "Hola "
b = "Python"

print(a + b)

# Way number 3
greet, language = "Hola", "Python"
print(greet,language)


print("Exercise 3")
#3. Crea una cadena que incluya un salto de línea, y luego imprímela para ver el resultado.

# Para hacer un salto de linea hay que tipear \n

my_string = "LOS POYITOS DICEN PIO PIO \n CUANDO TIENE HAMBRE Y CUANDO TIENEN FRIO"
print(my_string)

my_second_string = "Anuel AA y Westcol son mis \ndos personajes famosos favoritos."
print(my_second_string)


print("Exercise 4")
# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
"""
%s - String (or any object with a string representation, like numbers)
%d - Integers (Para numeros)
%f - Floating point numbers (Para decimales)
"% - number of digitsf" - Floating point numbers with fixed precision

"""
date, name, surname, age, = 31, "Alejandro", "Castellano", 22
                                                                                                                                                #Tenemos dos formas de trabajar
print("Buenas tardes hoy es %d de enero del 2026, mi nombre es %s %s y tengo %d años de edad." %(date, name, surname, age))                 

print("Buenas tardes hoy es {} de enero del 2026, mi nombre es {} {} y tengo {} años de edad." .format(date, name, surname, age))               #Esta es la mejor....


name, surname, age, date = "Jhon", "Dohe", 25, 2024

print("%s %s tiene %d años y su fecha registrada es %d." %(name, surname, age, date))

print("{} {} tiene {} años y su fecha registrada es {}.". format(name, surname, age, date))


print("Exercise 5")
# 5. Desempaqueta los caracteres de la palabra “Alejandro” en variables separadas y luego imprímelos uno por uno.

"""
#Texto de impresión: Python

lenguage_slice = lenguage[1:3]                  #Toma los letras exactas de nuestra variable
print(lenguage_slice)

lenguage_slice = lenguage[1:]                   #Pilla las letras desde donde empieza hasta el final
print(lenguage_slice)

lenguage_slice = lenguage[-2]                   #Es la o ya que empieza desde el final entonces n es -1 & o es -2
print(lenguage_slice)

# Reverse
print("Reverse")

#Texto de impresión: Python
reversed_lenguage = lenguage[::-1]              #Para imprimir el texto de atras para adelante
print(reversed_lenguage)

lenguage_slice = lenguage[1:2:4]
print(lenguage_slice)

lenguage_slice = lenguage[0:6:2]
print(lenguage_slice)

"""

nationality = "Ecuadorian"

a,b,c,d,e,f,g,h,i,j = nationality

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)

nationality_slice = nationality [0:3]
print(nationality_slice)

nationality_slice = nationality [::-1]
print(nationality_slice)

nationality_slice = nationality [5:]
print(nationality_slice)

nationality_slice = nationality [-6]
print(nationality_slice)


print("Exercise 6")
# 6. Extrae un “slice” de la palabra “Programación” para obtener los caracteres desde la posición 3 hasta la 7.

word = "Programación"

print(len(word))

a,b,c,d,e,f,g,h,i,j,k,l = word

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)

word_slice = word [3:8]                     #Nos pide hasta la pocision 7 entonces debemos colocar un numero mas siempre ya que se empieza a contar desde el inicio del string desde 0
print(word_slice)


print("Exercise 7")
#7. Invierte la cadena “Python” usando slicing y muestra el resultado.

lenguage1 = "Python"
print(len(lenguage1))

a,b,c,d,e,f = lenguage1

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

lenguage_slice1 = lenguage1 [::-1]
print(lenguage_slice1)


print("Exercise 8")
#8. Convierte la cadena “aprendiendo python” en mayúsculas usando el método adecuado e imprímela.

"""
# Funciones
print("Funciones")

#Texto de impresión: Python
print(lenguage.capitalize())                    #Se utiliza para poner la primera letra en mayuscula
print(lenguage.upper())                         #Se utiliza para poner toda la letra en mayuscula
print(lenguage.count("h"))                      #Sirve para saber cuántas veces aparece un elemento específico.
print("78".isnumeric())                         #Es como una variable booleana para confirmar un tipo txto 
print("LALA".isnumeric())
print(lenguage.lower())                         #Para poner toda la variable en letras minusculas
print(lenguage.upper().isupper())               #Se hizo una combinacion primero se coloco todas las letras en mayuscula y luego se metio una var booleana para confirmar si todas las letras son mayusculas therefore is true
print(lenguage.lower().isupper())               #Es falsa por que no cumple con el isupper
print(lenguage.startswith("Py"))                #Es verdadero a que la variable lenguage: Python si empieza asi
print(lenguage.startswith("py"))                #Es falso ya que no empieza con py sino con Py
print("Py" == "py")

"""

text1 = "aprendiendo python"
print(text1.upper())

print(text1.capitalize())

text2 = "el mes de mayo fecha ya tu sabe"
print(text2.upper())
print(text2.capitalize())


print("Exercise 9")
#9. Cuenta cuántas veces aparece la letra “n” en la cadena “Programación en Python”.

text3 = "Programación en Python"

print(text3.count("n"))

text4 = "Hoy fui al mercado a comprar frutas y verduras."

print(text4.count("m"))
print(text4.count("o"))

print(text4.upper())
print(text4.capitalize())


print("Exercise 10")
#10. Verifica si la cadena “12345” es numérica usando el método adecuado e imprime el resultado.

#print("78".isnumeric())                         #Es como una variable booleana para confirmar un tipo txto 
#print("LALA".isnumeric())

my_string1 = "12345"

print(my_string1.isnumeric())

my_string2 = "LALA"
print("LALA".isnumeric())