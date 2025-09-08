# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.

nombre = input("Ingresa tu nombre: ").capitalize()
apellido = input("Ingresa tu apellido: ").capitalize()
edad = int(input("Ingresa tu edad: "))
lugar = input("Ingresa tu lugar de residencia: ").capitalize()

print(f"Soy {nombre} {apellido}, tengo {edad} {'años' if edad != 1 else 'año'} y vivo en {lugar}")
