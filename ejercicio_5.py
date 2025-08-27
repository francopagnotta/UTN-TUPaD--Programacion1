# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundos = int(input("Ingresa una cantidad de segundos: "))
horas = round(segundos / 3600, 2)

print(f"{segundos} segundos equivalen a {horas} horas")
