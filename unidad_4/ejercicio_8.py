# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

NUMBER_COUNT = 100
even_count = 0
odd_count = 0
positive_count = 0
negative_count = 0

for i in range(NUMBER_COUNT):
    number = int(input(f"Ingresa un numero entero, ingresaste {i} de {NUMBER_COUNT}: "))

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1

print(f"numeros pares: {even_count}")
print(f"numeros impares: {odd_count}")
print(f"numeros positivos: {positive_count}")
print(f"numeros negativos: {negative_count}")
