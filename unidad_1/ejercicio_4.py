# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

import math

radio = float(input("Ingrese el radio del círculo: "))
area = round(math.pi * radio ** 2, 2)
perimetro = round(2 * math.pi * radio, 2)

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")
