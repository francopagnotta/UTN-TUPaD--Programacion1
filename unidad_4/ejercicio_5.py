# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

attempts = 0
random_number = random.randint(0, 9)
print(random_number)
stop_loop = False

while not stop_loop:
    user_input = int(input("Ingrese un numero aleatorio entre 0 y 9: "))

    if user_input == random_number:
        print("ganaste")
        stop_loop = True
    else:
        print("Ups, numero incorrecto")
