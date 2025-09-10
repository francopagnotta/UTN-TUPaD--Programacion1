# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

vowels = ['a', 'e', 'i', 'o', 'u']

userInput = input("ingrese un string: ").lower()

lastWord = userInput[len(userInput) - 1]

if lastWord in vowels:
    print(f"{userInput}!")
else:
    print(userInput)

