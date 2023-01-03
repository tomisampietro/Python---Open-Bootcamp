#El uso del * para importar no es eficiente, tiene un gran costo logico.
from Paquete.calculadora_simple import *

def main():
    division(10,2)

    #Instanciar la clase Multiplicador
    op = Multiplicador()
    op.multiplicacion(4,2)

#    print(como_me_llamo())

if __name__ == "__main__":
    main()
