# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Escribir un programa que pregunte al usuario en cuál emisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisphere = input("¿En qué hemisferio te encuentras? (N/S): ").lower()
month = int(input("¿Qué mes del año es en numero? "))
day = int(input("¿Qué día del mes es en numero? "))

if hemisphere == "n":
    if month == 12 and day >= 21 or month == 1 or month == 2 or month == 3 and day <= 20:
        print("¡Estás en Invierno!")
    elif month == 3 and day >= 21 or month == 4 or month == 5 or month == 6 and day <= 20:
        print("¡Estás en Primavera!")
    elif month == 6 and day >= 21 or month == 7 or month == 8 or month == 9 and day <= 20:
        print("¡Estás en Verano!")
    elif month == 9 and day >= 21 or month == 10 or month == 11 or month == 12 and day <= 20:
        print("¡Estás en Otoño!")
    else:
        print("Datos de fecha inválidos. Inténtalo de nuevo.")

elif hemisphere == "s":
    if month == 12 and day >= 21 or month == 1 or month == 2 or month == 3 and day <= 20:
        print("¡Estás en Verano!")
    elif month == 3 and day >= 21 or month == 4 or month == 5 or month == 6 and day <= 20:
        print("¡Estás en Otoño!")
    elif month == 6 and day >= 21 or month == 7 or month == 8 or month == 9 and day <= 20:
        print("¡Estás en Invierno!")
    elif month == 9 and day >= 21 or month == 10 or month == 11 or month == 12 and day <= 20:
        print("¡Estás en Primavera!")
    else:
        print("Datos de fecha inválidos. Inténtalo de nuevo.")

else:
    print("emisferio no reconocido. Por favor, ingresa 'n' o 's'")