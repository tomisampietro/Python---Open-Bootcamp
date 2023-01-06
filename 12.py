paises = input("Ingrese una lista de paises separe con coma: ")
lista_paises = paises.split(",")

lista_paises.sort()

print(set(lista_paises))