from io import open
archvo_vehiculo = open("vehiculo.txt", "w")

class Vehiculo():
    def __init__(self, puertas, hp):
        self.puertas = puertas
        self.hp = hp

auto = Vehiculo(2, 180)
mensaje = f"El auto tiene {auto.puertas} y produce {auto.hp}"
print(mensaje)

archvo_vehiculo.write(mensaje)
archvo_vehiculo.close()