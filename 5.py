a = int(input("Intorduzca un año: "))


if not a % 4 and (a % 100 or not a % 400):
    print(f"El año {a} es bisiesto")

else:
    print(f"El año {a} NO es bisiesto")