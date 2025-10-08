# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

NUMBER_COUNT = 100
total_sum = 0

for i in range(NUMBER_COUNT):
    number = int(input(f"Ingresa un numero entero, ingresaste {i} de {NUMBER_COUNT}: "))
    total_sum += number


average = total_sum / NUMBER_COUNT

print(f"La media de los valores ingreasdos es: {average}")
