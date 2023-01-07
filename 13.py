from functools import reduce

numeros = []
new_number = input("Ingrese una lista de numeros, separados por coma: ")

agrego_a_lista = new_number.split(",")
numeros.extend(agrego_a_lista)

int_numbers = []
for n in numeros:
    int_numbers.append(int(n))

def es_impar(n):
    return n % 2 == 1

lista_impares = filter(es_impar,int_numbers)
print(f"su lista de numeros impares es {list(lista_impares)}")

def suma(a,b):
    return a+b

if not lista_impares:
    print("No hay numeros impares en la lista.")
else:
    suma_lista_impares = reduce(suma,lista_impares)
    print(f"La suma de los numeros impares de la lista es: {suma_lista_impares}")