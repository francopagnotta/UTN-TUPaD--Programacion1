# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

user_input = input("Ingresa un numero entero: ")

reversed_number = user_input[::-1]

print(f"El numero ingresado es: {user_input}")
print(f"El numero invertido es: {reversed_number}")
