# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

result = 0
stop_loop = False

while not stop_loop:
    user_input = int(
        input("Ingrese un numero entero para sumar o 0 para terminar el programa: ")
    )

    if user_input == 0:
        print(f"El resultado de la suma es: {result}")
        stop_loop = True

    else:
        result = result + user_input
