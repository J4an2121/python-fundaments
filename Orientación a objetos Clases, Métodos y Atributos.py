# Una CLASE es como un plano o molde para crear objetos.
# Define las características (atributos) y comportamientos (métodos).

# ATRIBUTOS -> Son variables que pertenecen a la clase u objeto.
    # Guardan información de cada objeto creado.

# MÉTODOS -> Son funciones dentro de una clase.
    # Describen las acciones que los objetos pueden realizar.

#Clase → Plano o molde para crear objetos.

#Atributos → Variables propias de un objeto (características).

#Métodos → Funciones dentro de la clase (acciones).

#Objeto → Una instancia concreta creada a partir de la clase.

class Coche:

    def __init__(self , vel_max, color):
        self.max_vel = vel_max
        self.color = color

    def velocidad_maxima(self):
        print("La velocidad máxima: ", self.max_vel ,self.color) 

coche1 = Coche(200, "rojo")

coche1.velocidad_maxima()

coche2 = Coche(300, "azul")

coche2.velocidad_maxima()

