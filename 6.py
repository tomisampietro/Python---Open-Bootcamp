class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color  
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    pass #los atributos se definen en el constructor.
    def __init__(self, velocidad, cilindrada):
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def descripcion(self):
        return "Anda a una velocidad maxima de {} y tiene {} cc".format(self.velocidad, self.cilindrada)

#Creo un objeto "a"
a = Coche("250km/h", 1000)
print(a.descripcion())

