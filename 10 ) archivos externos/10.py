from io import open

texto_plano = open("nuevo_archivo.txt", "w")

frase = "Hola me llamo Tomas."

texto_plano.write(frase)
texto_plano.close()

texto_plano = open("nuevo_archivo.txt", "r")
lectura = texto_plano.read()

texto_plano.close()

print(lectura)


