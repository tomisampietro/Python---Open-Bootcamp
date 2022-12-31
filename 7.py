class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def show_nombre(self):
        return "{}".format(self.nombre)

    def show_nota(self):
        return "{}".format(self.nota)
    
    def definicion(self):
        if self.nota >= 7:
            return "{} ha aprobado. Su nota es: {}".format(self.nombre, self.nota)
        else:
            return "{} no ha aprobado. Su nota es {}".format(self.nombre, self.nota)

a = Alumno("Sampietro", 10)
print(a.show_nombre())
print(a.show_nota())
print(a.definicion())