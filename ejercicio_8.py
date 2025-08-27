# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.

altura = float(input("Ingresa tu altura en metros: "))
peso = float(input("Ingresa tu peso en kg: "))
imc = round(peso / (altura ** 2), 2)

print(f"IMC = {imc}")
