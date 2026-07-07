### Modules ###

"""
Los modulos en python nos permiten dividir el codigo en archivos separados
y organizados, lo que facilita la legibilidad y reutilizacion.

Un modulo en python es simplemente un archivo que contine funciones, variables
y otras definiciones, y que podemos importar en otros archivos para utilizar su
contenido. Python ofrece una fran variedad de modulos predefinidos que cubren
muchas funcionalidades, como operaciones matematicas, manejo de archivos y mas
pero tambien podemos crear nuestros propios modulos personalizados.

Los modulos son esenciales para mantener el codigo organizado y reutilizable.
En lugar de tener un solo archivo gigante con todo tu codigo, puedes dividir las
funcionalidades en diferentes archivos (modulos) y luego importarlos donde los
necesites, esto hace que el codigo sea mas facil de mantener, escalar y depurar.
 
"""

# from 10_functions import sum_two_values        ----> Esto nos da error ya que los ficheros para modulos no deben estar encabezados por un numero (Sintaxis que no le vale a Python)

import module                      #Impota todo los que hay dentro del nuestro archivo module
             
module.sum(3, 5, 88)                          #Para llamar a la funcion de nuestro modulo si la importamos en concreto es decir todo el modulo
module.printValue("Hola Python!!!")           #Para importar una operacion concreta de nuestro modulo 


from module import printValue,sum 
sum(10, 10, 10)
printValue("KLK empezoo el veranoo")
                    

import math                             # Tenemos modulos que son del sistema por ejemplo math es un modulo de Python
print(math.pi)
print(pow(2, 8))                        # 2 elevado a la 8 potencia
print(math.pow(3, 3))                   # El pow se usa como potencia


from math import pi as El_PIPIvalue          # Asi nosotros damos el nombre a la funcion que importamos

print(El_PIPIvalue)

from math import sqrt                   # Para calcular la raiz cuadrada de un numero
print(sqrt(30))

from math import cbrt                   # Para calcular la raiz cubica de un numero
print(cbrt(27))

print(sqrt(3)/2)

#print(9*sqrt(3)/2)
#print(-9*sqrt(3)/2)

#Para que el ususario digite un numero y le devuelva la raiz

#from math import sqrt
# numero = float(input("Ingresa un numero:"))
#print("La raiz es", sqrt(numero))

# graficar_vector(sqrt(3)/-2)     -----> para calcular una raiz positiva
# graficar_vector(-sqrt(3)/4)     -----> para calcular una raiz negativa

# graficar_vector(-(9/2), 9*np.sqrt(3)/2)           #Se usa esto para graficar dos puntos de vectores en R2


#EXCERCICES.PY11``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

print("EJERCICIOS")


print("Exercise 1")
# 1. Crea un módulo llamado "calculator" que contenga funciones para sumar, restar, multiplicar y dividir dos números. Importa este módulo en otro archivo y usa sus funciones.

import Mcalculator1

Mcalculator1.sum_two_values(28, 32)
Mcalculator1.rest_two_values(50, 25)
Mcalculator1.multip_two_values(7, 7)
Mcalculator1.div_two_values(27, 3)

from Mcalculator1 import sum_two_values

sum_two_values(200, 300)



print("Exercise 2")
# 2. Crea un módulo llamado "converter" que tenga funciones para convertir temperaturas entre Celsius y Fahrenheit. Escribe un programa que importe este módulo y realice conversiones.

import Mconverter2

print(Mconverter2.farenheit_a_celsius(108))              # Como usamos return el resultado queda solo guardado, entonces debemos usar en estos casos print para enseñarlo en pantalla.
print (Mconverter2.celsius_a_ferenheit(45))


from Mconverter2 import farenheit_a_celsius, celsius_a_ferenheit

print(farenheit_a_celsius(108))
print(celsius_a_ferenheit(45))



print("Exercise 3")
# 3. Crea un módulo que contenga una lista de nombres de estudiantes y una función que imprima todos los nombres. Importa este módulo en otro archivo y usa la función para mostrar la lista.

import Mestudiantes3

Mestudiantes3.show_students()

print('Lista 2')
from Mestudiantes3 import show_students

show_students()



print("Exercise 4")
# 4. Crea un módulo llamado "geometry" que tenga una función para calcular el área de un círculo y un cuadrado. Usa este módulo en otro archivo para calcular áreas.

import Mgeometry4

print(Mgeometry4.calcular_area_circulo(10))

print(Mgeometry4.calcular_area_cuadrado(20))



print("Exercise 5")
# 5. Escribe un módulo que contenga una función que acepte cualquier número de argumentos y devuelva su suma. Importa y usa la función en otro archivo.

import Mmodule5

print(Mmodule5.sumar(34,34,32))     #Usamos el print porque nuestra funcion usaba el return


from Mmodule5 import sumar

print(sumar(20, 25, 15))



print("Exercise 6")
# 6. Crea un módulo que defina una clase llamada "Car" con propiedades como marca, modelo y año. Importa este módulo en otro archivo y crea una instancia de la clase "Car".

import Mmodulecar6

mi_carro = Mmodulecar6.Car("Toyota", "Corolla", 2020)
mi_carro2 = Mmodulecar6.Car('Honda','Civic', 2022)

print(mi_carro.marca)
print(mi_carro2.modelo)



print("Exercise 7")
# 7. Escribe un módulo que contenga funciones para leer y escribir en archivos de texto. Crea un programa que use estas funciones para escribir y leer datos.

import Mmodulefile_manager7

Mmodulefile_manager7.escribir_archivo("My_notesAlejandro.txt", "Hola Python soy y estoy aprendiendo a utilizar los modulos")

Mmodulefile_manager7.leer_archivo("My_notesAlejandro.txt")



print("Exercise 8")
# 8. Crea un módulo llamado "statistics" que tenga funciones para calcular la media y la mediana de una lista de números. Usa este módulo para calcular estos valores en una lista dada.

import Mmodulestatics8

numeros = [10, 20, 30, 40, 50]                              # Aqui podemos pasar cual quier tipo de lista y calcularla de manera automatica

print(Mmodulestatics8.calcular_media(numeros))              # El promedio la suma de todo dividido para la cantidad de elementos

print(Mmodulestatics8.calcular_mediana(numeros))            # El numero de la mitad



print("Exercise 9")
# 9. Crea un módulo que contenga una función para contar cuántas veces aparece una palabra en un texto. Escribe un programa que importe el módulo y lo use para contar palabras en una cadena.

import Mmodulewords9            # Contador de palabras

print(Mmodulewords9.contar_palabras(texto="python es divertido y python es facil de aprender porque python tiene una sintaxis sencilla", palabra="python"))



print("Exercise 10")
# 10. Crea un módulo llamado "dates" que contenga funciones para obtener la fecha actual y calcular la diferencia entre dos fechas. Usa este módulo en un programa para mostrar la fecha actual y la diferencia entre dos fechas específicas.

import Mmodulydates10
import datetime

print(Mmodulydates10.fecha_actual())

fecha1 = datetime.datetime(2024, 1, 1)          #Usamos el formato AÑO, MES, DIA
fecha2 = datetime.datetime(2024, 1, 10)

print(Mmodulydates10.diferencia_fechas(fecha1, fecha2))


#CONGRATULATIONS JHOEL ALEJANDRO HEMOS FINALIZADO NUESTRO PRIMERO CURSO DE PROGRAMACION


 