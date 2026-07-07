
class Car:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        pass
    
# my_car = Car ('Toyota','Corolla', 2020)           Esto ya no es necesario colocar en este apartado
# my_car2 = Car ('Honda','Civic', 2022)             ya que en nuestro mudolo solo necesitamos la estructura
#                                                   de nuestra clase y ya solo lo usamos en donde vamos a
#print(my_car.marca)                                trabajar en nuestro archivo principal y ahi decidimos que
#print(my_car2.marca)                               objetos crear apartir del numero de elementos que creamos
#                                                   en nuestra clase.