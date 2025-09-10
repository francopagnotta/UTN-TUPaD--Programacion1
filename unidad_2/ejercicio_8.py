# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

userName = input("ingrese su nombre: ")
option = int(input("ingrese 1 para su nombre en mayusculas, 2 para minusculas o 3 para primera letra mayuscula: "))

match option:
    case 1: print(userName.upper())
    case 2: print(userName.lower())
    case 3: print(userName.title())
    
    