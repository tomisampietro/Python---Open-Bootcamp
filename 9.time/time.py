
import time

ahora = time.strftime("%H")

if int(ahora) < 19:
    print("trabajo")
else:
    resto = int(ahora) -19
    print("Faltan:", resto, "horas para irse a casa")
