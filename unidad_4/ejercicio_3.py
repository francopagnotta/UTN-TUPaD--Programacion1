# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

first_number = int(input("Ingrese el primer numero entero: "))
second_number = int(input("Ingrese el segundo numero entero: "))
result = 0

for i in range(first_number + 1, second_number):
    result = result + i

print(result)
