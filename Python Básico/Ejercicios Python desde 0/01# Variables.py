# Variables

'''
Las variables son uno de los conceptos basicos de la programacion,
ya que nos permiten almacenar y manipular datos. Una variable no es
mas que un nombre que asocia un valor especifico, y en Python, su 
uso es muy flexible lo que facilita su aprendizaje.

Recibir datos del usuario: Usamos input() para pedirle informacion
al usuario, y que ocurre si cambiamos el tipo de una variable despues
de haberla definido.

'''


my_variable= "My Strign Variable"
print(my_variable)

my_int_var= 5
print(my_int_var)

my_bool_var= True
print(my_bool_var)


#Concatenacion de variables en print
print(my_bool_var,my_variable,my_int_var)
print('Este es el valor de mi variable:',my_int_var)


#Transformar una variable entera a texto
print('Transformar una variable entera a texto')
my_int_var= 8
print(my_int_var)

my_int_to_str_var= str(my_int_var)
print(my_int_to_str_var)
print(type(my_int_to_str_var))
print(type(my_int_var))

#Funciones del sistema
print(len(my_int_to_str_var))                   # Sirve para saber cuántos elementos hay en total en una estructura.
print(len(my_variable))                         # Funciona con listas, strings, tuplas, diccionarios, etc.

#Variables en una sola linea

name, surname, alias, age = "Alejandro","Caste","Niño", 22
print("Me llamo:", name, surname,". Mi edad es:",age, ". Y mi alies es:", alias)

# Inputs
"""
name = input('Whats your name:')
age = input('How old are you?')

print(name, age)
"""

#Cambiamos su tipo
name = 25
age = "Alejandro"

print(name)
print(age)

# Forzamos el tipo
print("Klk mgv")

address: str = "Mi dirección"
address = 32
print(address)
print(type(address))


print("EJERCICIOS")

print("Exercise 1")

# 1. Declara y asigna valores a las siguientes variables:
# â€¢	name: una cadena que contenga tu nombre.
# â€¢	age: un nÃºmero entero que represente tu edad.
# â€¢	height: un nÃºmero flotante que represente tu altura.
# â€¢	Imprime cada variable en una lÃ­nea separada.

name= 'Alejandro'
age= 22
height= 170.1

print("Nombre:",name)
print("Edad:", age)
print("Altura:", height)

print("Exercise 2")
# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuántos años tienes.
"""
#Transformar una variable entera a texto

print('Transformar una variable entera a texto')
my_int_var= 8
print(my_int_var)

my_int_to_str_var= str(my_int_var)
print(my_int_to_str_var)
print(type(my_int_to_str_var))
"""

my_var_age = 22
print("Tengo",my_var_age,"añitos crezco muy despacito.")

my_var_age_to_str_var_age = str(my_var_age)
print(my_var_age_to_str_var_age)
print(type(my_var_age_to_str_var_age))

my_age_var = 29
print('Yo precioso tengo:',my_age_var,'añitos de edad.')

my_age_var_to_my_str_var= str(my_age_var)
print(my_age_var_to_my_str_var)

print(type(my_age_var_to_my_str_var))

my_age_stalin= 24
print("Hola soy stalin y tengo", my_age_stalin, "años de edad.")

my_age_stalin_to_my_str_stalin= str(my_age_stalin)
print(my_age_stalin_to_my_str_stalin)

print(type(my_age_stalin_to_my_str_stalin))


print("Exercise 3")
# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False según corresponda e imprímela.

is_student= ["Ana", "Carlos", "María", "José", "Lucía","Martín"]

my_bool_1= "Ana","José","Martín", False
my_bool_2= "Carlos","María","Lucía", True

print("Son estudiantes:",my_bool_1)
print("Son estudiantes:",my_bool_2)


print("Exercise 4")
# 4. Usa la función len() para calcular cuántos caracteres tiene tu nombre completo, almacenado en una variable.

name= "Jhoel Alejandro Castellano Jácome"
print('Mi nombre completo es:', name)

print("Mi nombre completo tiene",len(name), "caracteres mas espacios.")

name2= ("Alejandro")
print('Mi nombre es:', name2)

print("Mi nombre tiene",len(name2), 'caracteres.')

surname2= 'Castellano'
print('My surname is:', surname2)

print("My surname have", len(surname2), 'characters.')


print("Exercise 5")
# 5. Declara tres variables en una sola línea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.

name, surname, borncity,= 'Alejandro','Castellano.', 'Sigchos'                   #Para hacer variables en una sola linea de ley se coloca primero todas las variables y luego las entradas de texto.
print('Hola mi nombre es',name, surname,'Mi cuidad de origen es', borncity)

name, age, height, surname, city,= 'Stalin','24',1.80,'Jacome', 'Uio'
print('Hola mi nombre es',name, surname, "Tengo",age,'añitos de edad. ''Mi cuidad de origen es', city)


print("Exercise 6")
# 6. Usa la función input() para solicitar al usuario su color favorito y almacénalo en una variable color. Luego, imprime el valor ingresado.

color= (input("Digite su color favorito:"))
print("Su color facorito es el:",color)


print(input("Digite su color favorito:"))


print("Exercise 7")
# 7. Declara una variable fruit e inicialízala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.

var_fruit= 89
print(var_fruit)

var_fruit = 189
print(var_fruit)

var_fruit2= "TORONJA"
print(var_fruit2)

var_fruit2= "Mandarina"
print(var_fruit2)


print("Exercise 8")
# 8. Convierte un número decimal, almacenado en la variable price, a un número entero y luego imprímelo.

var_price= 9.99
print(int(var_price))

var_price2= 6.66
print(int(var_price2))

var_price3= 3.14444
print(int(var_price3))

print("Exercise 9")
# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una dirección usando la función len(). Imprime el resultado.

address_len ="Carlos Hugo Páez y 7 de Agosto"
print('Mi direccion es:',address_len)

print('Mi dirección tiene la cantidad de',len(address_len), 'caracteres')

address_lento= "José Gabriel Terán y Sigchos"
print('Mi direccion es:',address_lento)

print('Mi dirección tiene la cantidad de',len(address_lento), 'caracteres')


print("Exercise 10")
# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurándote de que siempre será un número. Luego, cambia su valor a un número diferente y verifica el tipo de la variable con type().

var_phone: str= 'phonesofapple'

var_phone = 28
print(var_phone)
var_phone = 34
print(var_phone)
print(type(var_phone))


phone: int= 123456789
print(type(phone))

phone= 987654321
print(type(phone))

print("mmg")
str(5)
print(str)
print(type(str))

age1 = input("Cuantos anios tenes")

print(type(age1))

print("Hola", "Python")


#Para transformar una variable entera a texto

my_int26= 6
print(my_int26)

my_int26_to_string_26= str(my_int26)
print(my_int26_to_string_26)
print(type(my_int26_to_string_26))
