### Clases ###

"""
Las clases son la base de la creacion de objetos y nos permiten estructurar nuestro
codigo de manera mas organizada.
Una clase en python es como un plano o molde para crear objetos. Define las 
caracteristicas (atributos) y comportamientos (métodos) que los objetos derivados 
de esa clase tendrán. Esto nos permite trabajar de manera más eficiente con datos 
complejos, organizando nuestro código en unidades más manejables.

Las clases son fundamentales porque oermiten agrupar datos y comportamientos en una
sola unidad lógica. Esto no solo ayuda a organizar mejor el código sino que también
te permite reutilizarlo fácilmente. Además, las clases son clave para trabajar con
programación orientada a objetos (OOP o POO), un paradigma que ayuda a crear software
más flexible y escalable.

"""
#Una instacia es un objeto creado apartir de una clase

class MyEmptyPerson:                     # Los nombres de las clases se escriben en CamelCase la primera letra en mayuscula sin espacios y sin guiones esto para que considere como buenas practicas
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())


class Person:
    def __init__(self, name, surname, age):                     #Se usa para que la funcion pueda recibir parametros
        self.name = name
        self.surname = surname                                  #El uso de self es obligatorio porque este almacena la variable
        self.age = age
        pass
    
    
my_person = Person('Alejandro', 'Castellano', 22)
print(my_person.name)
print(my_person.surname)
print(my_person.age)

print(f'{my_person.name} {my_person.surname} {my_person.age}')                  # Otra forma de imprimir en cadena de texto



class SecondPerson:
    def __init__(self, name, secondname, surname, secondsurname):
        self.name = name
        self. surname = surname
        self. secondname = secondname
        self. secondsurname = secondsurname
        pass
    
my_secondperson = SecondPerson('Jhoel', 'Alejandro', 'Castellano', 'Jacome')
print(my_secondperson.name)
print(my_secondperson.secondname)
print(my_secondperson.surname)
print(my_secondperson.secondsurname)

print(f'{my_secondperson.name} {my_secondperson.secondname} {my_secondperson.surname} {my_secondperson.secondsurname}')


class ThirdPerson:
    def __init__(self, name, secondname, surname, secondsurname):
        self.full_data = f'{name} {secondname} {surname} {secondsurname}'
        
my_people = ThirdPerson ('Jh', 'Alejand', 'Castel', 'Jaco')
print(my_people.full_data)



class SecondPerson1:
    def __init__(self, name, surname):
        self.full_name = f'{name} {surname}'                    # haciendo de esta manera es facil y mas practico en cuanto a eficiencia
        
    def walk(self):                                             # siempre para crear una nueva funcion utilizamos el self
        print(f'{self.full_name} esta caminando')
        
my_person1 = SecondPerson1 ('Alejandro', 'Magno')
print(my_person1.full_name)
my_person1.walk()


print('Ejemplo con valores por default')
class SecondPerson1:
    def __init__(self, name, surname, alias = 'Sin alias'):                       #Tambien se pueden añadir valores por defecto x ejemplo en un alias
        self.full_name = f'{name} {surname} (***{alias}***)'                    
        
    def walk(self):                                             # 
        print(f'{self.full_name} esta caminando')
        
my_person1 = SecondPerson1 ('Alejandro', 'Magno')
print(my_person1.full_name)
my_person1.walk()


my_other_person = SecondPerson1('Alejandro', 'Magno', 'Elpingon')
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = 'Hector el (Father)'                        #Aqui formateamos la funcion x lo tanto esta es una nueva cadena
print(my_other_person.full_name)



# Para hacer que un valor sea privado
# Si intentas acceder a un atributo privado directamente genera un AttributeError

print('Ejemplo con valores por default')


class SecondPerson1:
    def __init__(self, name, surname, alias = 'Sin alias'):                       #Tambien se pueden añadir valores por defecto x ejemplo en un alias
        self.full_name = f'{name} {surname} (***{alias}***)'   #Propiedad publica                 
        self.__name = name   #Propiedad privada
        
    def get_name (self):
            return self.__name
        
    def walk(self):                                             # 
        print(f'{self.full_name} esta caminando')
        
my_person1 = SecondPerson1 ('Brais', 'Mouredev')
print(my_person1.full_name)
print(my_person1.get_name())
my_person1.walk()

#Ejemplo de repaso

class Culaguanin:
    def __init__(self, nombre, curso, CI, Age):
        self.fullstack = f'{nombre}, {curso}, {CI}, {Age}'
        self.__nombre = nombre
    def get_name (self):
        return self.__nombre
        pass
    
my_stack = Culaguanin ('Alejandro', 'firstsemester', '0504147208',22)
print(my_stack.fullstack)
print(my_stack.get_name())



#EXCERCICES.PY11``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

print("EJERCICIOS")


print("Exercise 1")
# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y un método "make_sound" que imprima un sonido genérico.

class Animal:
    def __init__(self, species):
        self.species = species          # propiedad
        
    def make_sound(self):
        print('Sonido generico')        # metodo
        pass
    
animal1 = Animal('perro')
animal1.make_sound()

print("Exercise 2")
#2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacénala en una propiedad pública. Añade el método "make_sound" que imprima un sonido dependiendo de la especie.

class Animal2:
    def __init__(self, species):
        self. species = species
        
    def make_sound(self):
        if self.species == 'Gallina':
            print("kikiriki")
        elif self.species == 'Perro':
            print('guau, guau, guau')
        elif self.species == 'Gato':
            print('miuau miau miau')
            
        else:
            print('Sonido animal generico')
        pass
    
sound1 = Animal2('Perro')
sound1.make_sound()

sound2 = Animal2 ('Gallina')
sound2.make_sound()

sound3 = Animal2 ('Gato')
sound3.make_sound()

print("Exercise 3")
#3. Crea una clase llamada "Car" con las propiedades públicas "brand" y "model". Además, debe tener una propiedad privada "_speed" que inicialmente será 0.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
        self.__speed = 0
        pass


print("Exercise 4")
#4. Añade a la clase "Car" un método llamado "accelerate" que aumente la velocidad en 10 unidades. Añade también un método "brake" que reduzca la velocidad en 10 unidades. Asegúrate de que la velocidad no sea negativa.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
        self.__speed = 0
        
    def accelerate(self):
        self.__speed += 10
        pass

    def brake(self):
        self.__speed = (0,self.__speed - 10)



print("Exercise 5")
#5. Crea una clase "Book" que tenga propiedades como "title" (público) y "author" (privado). Añade un método para obtener el autor y otro para cambiar el título del libro.


class Book:
    def __init__(self, title, author):                  # este es el ejemplo practico mas completo please check
        self.title = title
        self.__author = author
        
    def get_author (self):
        return self.get_author
    
    def change_title(self, new_title):
        self.title = new_title
        
        
        
print("Exercise 6")
# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. Añade un método para calcular y devolver la nota media del estudiante.

class Estudiante:
    def __init__(self, Nombre, Apellido, Notas):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Notas = Notas
        
    def calculate_promedio(self):
        return sum(self.Notas) / len(self.Notas)                    #para devolver la nota media
        
    
    
print("Exercise 7")
# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". Añade métodos para depositar y retirar dinero, asegurándote de que no se pueda retirar más de lo que hay en la cuenta.

class BankAccount:
    def __init__(self, owner, balance):                 #self toma cada valor como cerebro o base principal es decir tiene acceso a cada uno de los elementos dentro de self
        self.owner = owner
        self.balance = balance
        
    def depositar(self, cantidad):                      # funcion para crear depositos
        self. balance += cantidad
        
    def retirar(self, cantidad):                        # para retirar dinero
        if cantidad <= self.balance:                    # Si lo que quiero retirar es menor o igual al saldo disponible
            print('Retiro Exitoso') 
            self.balance -= cantidad
        elif cantidad > self.balance:
            return 'Saldo insuficiente'
            
        else:
            print('Saldo insuficiente')



print("Exercise 8")
# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". Añade un método que calcule la distancia entre dos puntos.

class Point:
    def __init__(self, x, y):
        self. x = x
        self. y = y
        
    def distancia(self, otro_punto):
        distance_x = self.x - otro_punto.x
        distance_y = self.y - otro_punto.y
        
        return (distance_x**2 + distance_y**2)**0,50                # raiz cuadrada


p1 = Point (0, 0)
p2 = Point (3,4)

print(p1.distancia(p2))



print("Exercise 9")
# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked". Añade un método que calcule el pago total basado en las horas trabajadas y el salario por hora.
class Employee:
    def __init__(self, name, hourly_wage, hours_worked):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def calculate_total_pay(self):
        return self.hourly_wage * self.hours_worked
    
paycheck1 = Employee('Juan', 12.50, 40)

totalpay = paycheck1.calculate_total_pay()

print(f'El pago total de {paycheck1.name} es: {totalpay}')



print("Exercise 10")
# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). Añade un método para agregar un producto al inventario y otro para mostrar todos los productos disponibles.

class Store:
    def __init__(self, inventory):                      # Para crear un inventario
        self.inventory = []
        
    def add_product(self, product):
        self.inventory.append(product)                  # Para añadir productos a la lista del inventario
        
    def show_inventory(self):                           # Moatrar todos los elementos dentro de la lista disponibles
        for product in self.inventory:
            print(product)
            

