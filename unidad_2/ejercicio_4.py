# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# - Niño/a: menor de 12 años.
# - Adolescente: mayor o igual que 12 años y menor que 18 años.
# - Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# - Adulto/a: mayor o igual que 30 años.

age = int(input("Ingrese su edad: "))

if age >= 12 and age <= 18:
    print("Adolescente")
elif age >= 18 and age < 30:
    print("Adulto/a joven")
elif age >= 30:
    print("Adulto/a")
else:
    print("Niño/a")