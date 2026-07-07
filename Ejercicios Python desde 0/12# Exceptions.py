#### Exception Handling ###

"""
Las excepciones son errores que pueden ocurrir durante la ejecucion de un programa
y el manejo adecuado de estos errorres es crucial para evitar que nuestros programas
se detengan inesperadamente.

En Python el manejo de excepciones nos permite anticiparnos a posibles errores y controlarlos
de manera eficiente, proporcionando una experiencia mas fluida al usario y manteniendo la 
estabilidad del programa.

El manejo de estas excepciones es fundamental ya que nos perimite construir programas
mas robustos. Ningun programa esta libre de errores pero si estos se manejan de manera 
adecuada, podemos prevenir que el usuario final se vea afectado y garantizar que el 
programa siga funcionando.

"""

# print(5 + "5")                    esto daria un error ya que es un numero mas una cadena de texto

numberone = 5 
numbertwo = 1
numbertwo ='1'                      # Usamos las excepciones para controlar este tipo de errores y que el programa no se muera


# try except

try:
    print (numberone + numbertwo)
    print ("No se ha producido un error")
except:
    # Se ejecuta si se ha producido una excepcion 
    print("Se ha producido un error")

# try except else finally

try:
    print (numberone + numbertwo)
    print ("No se ha producido un error")
except:
    print("Se ha producido un error")

else:                                           
     # El bloque de codigo else se ejecuta solo si no se ha producido un error
    print('La ejecucion continua correctamente')
    
finally:
    # Se ejecuta siempre
    print("La ejecucion continua")

# El programa funciona normalmente, sin poner else o finally sin problema pero siempre debe ir el try y el except


# Captura de excepciones por tipo
print('Captura de excepciones por tipo')

try:
    print (numberone + numbertwo)
    print ("No se ha producido un error")
except TypeError:                                   # Se ejecuta solo si se produce errores de tipo TypeError
    print("Se ha producido un TypeError")
except ValueError:
    #(ValueError) este no le sirve ya que es otro tipo de error
    print('Se ha producido un ValueError')
    
    
    
# Captura de la informacion de la excepcion
print('Captura de la informacion de la excepcion')

try:
    print (numberone + numbertwo)
    print ("No se ha producido un error") 
except ValueError as alkes:                             # Por aqui no entra ya que no es el tipo de error que produce 
    print(alkes)
except Exception as error:                              # Este cumple con cualquier tipo de error que produzca por lo tanto ya no revienta el programa y continua funcionando
        # esta es una excepcion generica en la cual entra por cualquier tipo de error    
    print(error)
    
"""
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

TypeError → tipo de dato incorrecto
# ---> (ej: sumar número + texto)

int("hola")  # ❌

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

ValueError → tipo correcto, pero valor inválido
# ---> (ej: convertir "hola" a número)

"hola" + 5  # ❌ no puedes sumar texto con número

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

ZeroDivisionError
# 👉 División por cero

10 / 0  # ❌

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

NameError
# 👉 Usas una variable que no existe

print(x)  # ❌ x no está definida

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

IndexError
👉 Accedes a una posición que no existe en una lista

lista = [1, 2, 3]
print(lista[5])  # ❌

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

KeyError
👉 Accedes a una clave que no existe en un diccionario

dic = {"a": 1}
print(dic["b"])  # ❌

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

AttributeError
👉 Usas un método que no existe para ese tipo

"hola".append("a")  # ❌ los strings no tienen append

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

ImportError
👉 Error al importar algo

import no_existe  # ❌

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

FileNotFoundError
👉 Archivo no encontrado
open("archivo.txt")  # ❌ si no existe


"""


#EXCERCICES.PY12``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

print("EJERCICIOS")


print("Exercise 1")

# 1. Crea una función que intente dividir dos números proporcionados por el usuario. Usa try-except para capturar cualquier error de división (por ejemplo, división por cero).

def div_two_values (first_number, second_number):
    try:
        print(first_number / second_number)
        print ("No se ha producido un error")
    except:
        print("Se ha producido un error")
        
div_two_values(7,0)



print("Exercise 2")

#2. Crea una función que tome una cadena e intente convertirla en un número entero. Usa try-except para capturar cualquier error en la conversión.

def change_str_to_int (cadenadetexto):
    try:
        print(int(cadenadetexto))
        print("No se ha producido un error")
    except ValueError:
        print("Se ha producido un error")
        
change_str_to_int("hola")
change_str_to_int(12.5)
change_str_to_int(123)



print("Exercise 3")

# 3. Crea una función que abra un archivo, lea su contenido y maneje posibles errores (por ejemplo, archivo no encontrado). Usa try-except para gestionar las operaciones de archivos de forma segura.

def open_file(readfiles):                   # Aquí defines una función, readfiles es el nombre del archivo (por ejemplo "texto.txt")
    try:        #👉 Le dices a Python: "voy a intentar hacer algo que puede fallar"
        with open(readfiles, "r") as archivo:   #open(readfiles, "r") → abre el archivo en modo lectura ("r") (with ... as archivo → guarda el archivo en la variable archivo) → y lo cierra automáticamente después (esto es buena práctica)
            contenido = archivo.read()      # 👉 Aquí lees TODO el contenido del archivo 👉 y lo guardas en la variable contenido
            print(contenido)            # 👉 Muestras lo que había dentro del archivo
    
    except FileNotFoundError:           # Si el archivo no existe, Python entra aquí en vez de romper el programa
        print("Archivo no encontrado")  # Muestras un mensaje en lugar de que el programa falle
        
"""
🎯 Resumen simple

Tu función hace esto:

👉 “Intenta abrir un archivo y mostrar lo que tiene.
Si no existe, no se rompe: muestra un mensaje.”

"""



print("Exercise 4")

# 4. Crea una función que realice múltiples operaciones (suma, resta, división, multiplicación) con dos números. Usa try-except-else-finally para manejar errores y asegurar que se imprima un mensaje final, independientemente de los errores.

def operations(num1, num2):
    try:
        print("Suma:",(num1+num2))
        print("Resta:", (num1-num2))
        print("Multiplicación:", (num1*num2))
        print("División:", (num1/num2))
        
    except ZeroDivisionError:
        print("Error: Se ha producido un error. No se puede dividir entre 0")
        
    else:           # El bloque de codigo else se ejecuta solo si no se ha producido un error
        print('La ejecucion continua correctamente')
    
    finally:        # Se ejecuta siempre
        print('La ejecucion continua')
        
operations(30, 24)
operations(23, 50)



print("Exercise 5")

# 5. Crea una función que le pida al usuario su edad y lance un ValueError si la entrada no es un número entero positivo. Usa el manejo de excepciones para gestionar la entrada y lanzar excepciones personalizadas cuando sea necesario.

def pediredad():
    try:
        edad = int(input("Ingrese su edad:"))
        
        if edad <=0:
            raise ValueError("La edad deber ser positiva")          # raise se usa para lanzar (provocar) un error manualmente en tu programa.
        print("Edad valida", edad)
        
    except ValueError:
        print("Entrada Invalida:")

#pediredad()                 # Se debe llamar a la funcion si no esto solo estamos definiendo la funcion



print("Exercise 6")

# 6. Crea una función que intente acceder a un elemento de una lista por índice. Usa try-except para manejar el caso donde el índice esté fuera de rango.

def acceder_lista(lista, indice):
    try:
        print(lista[indice])
    
    except IndexError:
        print("Indice fuera de rango")

#              lista       indices
acceder_lista([10, 20, 30],  1)             #siempre los indices empiezan desde 0 es decir 0 es 10, 1 es 20, 2 es 30
acceder_lista([10, 20, 30],  5)             #el indice 5 no existe por lo tanto es un error
acceder_lista([10, 20, 30],  -1)

"""
Porque en Python los índices negativos son válidos.

Se usan para acceder desde el final de la lista:

-1 → último elemento
-2 → penúltimo
-3 → antepenúltimo

"""



print("Exercise 7")

# 7. Crea una función que use try-except para manejar múltiples excepciones: ZeroDivisionError, ValueError y TypeError.

def mi_funcion(a, b):
    try:
        num1 = int(a)
        num2 = int(b)
        print((num1 / num2))
        
    except ZeroDivisionError:
        print("No se puede divir por cero")
    
    except ValueError:
        print("Valor invalido")
    
    except TypeError:
        print("Tipos de datos incorrectos")
        

mi_funcion(7,0)
mi_funcion("hola", 999)
mi_funcion(None, 5)
mi_funcion(7,None)

'''
Forma fácil de diferenciar

"123" → válido
"hola" → ❌ ValueError
None → ❌ TypeError

'''



print("Exercise 8")

# 8. Crea una función que simule una transacción. Lanza una excepción personalizada llamada InsufficientFundsError si el saldo es menor que la cantidad a retirar.

class InsufficientFundsError(Exception):
    pass
def retirar(saldo, cantidad):
    try:
        if saldo < cantidad:    
            raise InsufficientFundsError("Fondos insuficientes")
        
        print ('Retiro exitoso')
        nuevo_saldo = saldo - cantidad                  #Para calcular un saldo final de una cuenta bancaria
        print(f"Su saldo es:{nuevo_saldo}")             # Para imprimir el nuevo saldo   
        
    except InsufficientFundsError as e:
            print(e)

retirar(100, 50)                                   # Es bien importante ver las posiciones de las lineas donde empiezan nuestras ffunciones ya que si no colocamos bien eso no se ejecuta la funcion
retirar(100, 150)
retirar(10000, 5500)



print("Exercise 9")

# 9. Crea una función que intente convertir una lista de cadenas en enteros. Maneja cualquier error que surja cuando una cadena no pueda convertirse.

def convert_list(my_list):              # Creamos una función que recibe una lista
    lista_convertida = []               # Aquí vamos a guardar los números válidos
    
    for element in my_list:             # Creamos un bucle for para recorrer la lista elemento por elemento
        
        try:
            numero = int(element)           # Utilizamos esto para convertir cada elemento a entero
            lista_convertida.append(numero)     # Utilizamos el append para agregar a la lista el valor convertido en este caso 10,20,30
        
        except ValueError:
            print("Error con:", element)
            
    return lista_convertida             # La función devuelve: [10, 20, 30]

convert_list(["10",'20','hola','30'])


"""
for → recorrer listas
try-except → manejar errores sin detener el programa
int() → conversión de datos
append() → guardar valores
return → devolver resultados

"""



print("Exercise 10")

# 10. Crea una función que calcule la raíz cuadrada de un número. Lanza un ValueError si el número es negativo.

def raiz_2(number):
    try:
        if number < 0:                                                      #  raise se usa para lanzar (provocar) un error manualmente en tu programa.
            raise ValueError('Error el numero debe ser positivo')           # Cuando la funcion nos pide que lanzemos un ValueError debemos utilizar el raise para generar un error
        
        result = (number**0.5)      #Para calcular raiz cuadrada
        print(result)
    except ValueError as e:
        print(e)
        
raiz_2(9)
raiz_2(27)
raiz_2(-70)

