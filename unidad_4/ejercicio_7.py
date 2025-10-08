# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

stop_loop = False
stop_range_number = 0
result = 0

while not stop_loop:
    user_input = input("Ingrese un numero entero positivo: ")

    if int(user_input) > 0:
        stop_range_number = int(user_input)
        stop_loop = True

for i in range(0, stop_range_number):
    print(i)
    result = result + i

print(f"resultado: {result}")
