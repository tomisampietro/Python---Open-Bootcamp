peso = input("Ingrese su peso en kg: ")
altura = input("Ingrese su altura en metros: ")

indice_masa_corporal = float(peso) / float(altura)
round(indice_masa_corporal,2)

print(f"Tu indice de masa corporal es {indice_masa_corporal}")