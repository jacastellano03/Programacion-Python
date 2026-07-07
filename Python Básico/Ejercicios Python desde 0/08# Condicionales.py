### Condicionales ###               # Permiten tomar decisiones basadas en codicionales logicos

'''
Los condicionales son una de las estructuras fundamentales en cualquier lenguaje de 
programacion, ya que permiten tomar desiciones basadas en condiciones logicas. En
Python, utilizamos principalmente las sentencias if, elif y else para controlar el 
flujo de ejecucion dependiendo de si una condicion se cumple o no.

Uso del --> (if, elif y else)
'''


# Principales condicionales en Python --> if, elif, else

                                    # Flujos de ejecucion de nuestro codigo, es decir representar si algo de nuestro codigo se va ejecutar o no
my_condition = False

if my_condition == True:            # Es lo mismo que if my_condition == True: (Es mejor si solo colocamos if my_condition:)
    print("Se ejecuta la condicion del if")

my_condition = 5 * 2

if my_condition == 11:
    print("Se ejecuta la condicion del segundo if")

if my_condition >= 10:
    print("Se ejecuta la condicion del tercer if")

if my_condition > 10:
    print("Es mayor que 10")
else:                                           # else --> Se utiliza para decir que haga algo sino se cumple la condicion
    print("Es menor o igual que 10")

if my_condition == 10:
    print("Se ejecuta la condicion del quinto if")


if my_condition > 10 and my_condition < 20:
    print('Es mayor que 10 y menor que 20')

else:
    print('Es menor o igual que 10 o mayor o igual que 20') 



print('Segundo Condicional')

my_condition2 =  4 * 5  # 4 * 5 = 20

if my_condition2 > 20 and my_condition2 < 30:
    print("Es mayor que 20 y menor que 30")

elif my_condition2 == 16:
    print('Es igual a 16')

else:
    print('Es menor o igual que 20 o mayor o igual que 30')


print('Examples with string 1')

my_string = 'Mi cadena de texto'

if my_string :
    print('Mi cadena de texto no es vacia')

if my_string == ('Mi cadena de textoooooppp'):
    print('Mis cadenas de texto coinciden')


print('Examples with string 2')

my_string = ''

if not my_string :
    print('Mi cadena de texto es vacia')


print('Examples with string 3')

my_string = 'Mi cadena de texto'

if my_string == ('Mi cadena de texto'):
    print('Mis cadenas de texto coinciden')


#EXCERCICES.PY08``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

print("EJERCICIOS")


print("Exercise 1")
# 1. Escribe un programa que verifique si un número es positivo, negativo o cero.

my_number = int(input('Introduce un numero:'))

if my_number > 0:
    print("Mi numero es positivo")

elif my_number < 0:
    print("Mi numero es negativo")

else:
    print("El numero es cero")



print("Exercise 2")
# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 años o más) o menor de edad.

age = int(input('Ingresa tu edad:'))

if age >= 18:
    print('Eres mayor de edad')

else:
    print('Eres menor de edad')


print("Exercise 3")
# 3. Escribe un programa que verifique si una cadena de texto está vacía y muestre un mensaje en consecuencia.

my_string = str(input('Introduce una cadena:'))

if not my_string:
    print('La cadena esta vacia')

else: 
    print('La cadena no esta vacia')



print("Exercise 4")
#4. Crea un programa que solicite dos números al usuario y compare cuál es mayor. Si son iguales, muestra un mensaje indicando la igualdad.

firstnumber = int(input('Inserta el primer numero:'))

secondnumber = int(input('Inserta el segundo numero:'))

if firstnumber > secondnumber:
    print('Mi primer numero es mayor que mi segundo numero')

elif secondnumber > firstnumber:
    print('Mi segundo numero es mayor que mi primer numero')

else:
    print('Ambos numeros son iguales')



print("Exercise 5")
# Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo.

number = int(input('Insete un numero:'))

if number % 3 == 0 and number % 5 == 0:                                     # Para cuando queramos comprobar si un numero es divisible para otro utilizamos el % y lo igualamos a 0 for example %3 == 0 u %5 == 0
    print("Mi numero es divisible para 3 y para 5")

else:
    print("Mi numero no es divisible para 3 y 5 al mismo tiempo")




print("Exercise 6")
# 6. Solicita al usuario que ingrese un número y verifica si es par o impar.

number1 = int(input('Ingresa un numero:'))

if number1 %2 == 0:
    print('Mi numero es PAR')

else:
    print('Mi numero en IMPAR')



print("Exercise 7")
#7. Escribe un programa que determine si una persona puede votar en función de su edad(mayor o igual a 18). Si tiene 16 o 17 años, indica que puede votar con permiso especial.

person = int(input('Ingrese su edad:'))

if person >= 18:
    print('Puede votar porque es mayor de edad')

elif person == 17 and person == 16:
    print('Pueden votar con permiso especial')

elif person == 16:
    print('Pueden votar con permiso especial')

else:
    print('No pueden votar')



print("Exercise 8")
# 8. Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida. Si no coincide, muestra un mensaje de error.

loggin = str(input('Ingrese su contraseña:'))

my_password = ('Shajaeea03')

if loggin == my_password:
    print("Acceso Correcto")

else:
    print('Acceso Denegado CONTRASEÑA INCORRECTA')



print("Exercise 9")
# 9. Escribe un programa que determine si un número está entre 10 y 20 (ambos incluidos).

number2 = int(input('Inserte un numero:'))

if number2 >= 10 and number <=20:
    print("Mi numero esta dentro de 10 y 20")

else:
    print("Mi numero no esta entre 10 y 20")



print("Exercise 10")
# 10. Escribe un programa que simule un semáforo: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.

semfcolor = str(input('Ingrese un color:'))

if semfcolor == ("Verde"):
    print("Puedes Avanzar")

elif semfcolor == ("Amarillo"):
    print("Debes estar Alerta")

elif semfcolor == ("Rojo"):
    print("Debes Detenerte")

else:
    print('Digite un color válido')



