# Trabajo Practico 11: Aplicacion de la Recursividad
# Franco Pagnotta - Comision 5


# Ejercicio 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def exercise_1():
    n = int(input("Ingrese un numero entero: "))
    
    print(f"\nFactoriales desde 1 hasta {n}:")
    for i in range(1, n + 1):
        result = factorial(i)
        print(f"Factorial de {i} = {result}")


# Ejercicio 2
def fibonacci(position):
    if position == 0:
        return 0
    if position == 1:
        return 1
    return fibonacci(position - 1) + fibonacci(position - 2)


def exercise_2():
    n = int(input("Ingrese la posicion hasta la cual mostrar la serie: "))
    
    print(f"\nSerie de Fibonacci hasta la posicion {n}:")
    for i in range(n + 1):
        value = fibonacci(i)
        print(f"Posicion {i}: {value}")


# Ejercicio 3
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


def exercise_3():
    base = float(input("Ingrese la base: "))
    exponent = int(input("Ingrese el exponente: "))
    
    result = power(base, exponent)
    print(f"\n{base} elevado a {exponent} = {result}")


# Ejercicio 4
def decimal_to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    
    quotient = n // 2
    remainder = n % 2
    
    return decimal_to_binary(quotient) + str(remainder)


def exercise_4():
    n = int(input("Ingrese un numero entero positivo: "))
    
    binary = decimal_to_binary(n)
    print(f"\nEl numero {n} en binario es: {binary}")


# Ejercicio 5
def is_palindrome(word):
    if len(word) <= 1:
        return True
    
    if word[0].lower() != word[-1].lower():
        return False
    
    return is_palindrome(word[1:-1])


def exercise_5():
    word = input("Ingrese una palabra (sin espacios ni tildes): ")
    
    if is_palindrome(word):
        print(f"\n'{word}' es un palindromo")
    else:
        print(f"\n'{word}' no es un palindromo")


# Ejercicio 6
def sum_digits(n):
    if n == 0:
        return 0
    
    last_digit = n % 10
    remaining = n // 10
    
    return last_digit + sum_digits(remaining)


def exercise_6():
    n = int(input("Ingrese un numero entero positivo: "))
    
    result = sum_digits(n)
    print(f"\nLa suma de los digitos de {n} es: {result}")


# Ejercicio 7
def count_blocks(n):
    if n == 1:
        return 1
    
    return n + count_blocks(n - 1)


def exercise_7():
    n = int(input("Ingrese el numero de bloques en el nivel mas bajo: "))
    
    total = count_blocks(n)
    print(f"\nEl total de bloques necesarios para la piramide es: {total}")


# Ejercicio 8
def count_digit(number, digit):
    if number == 0:
        return 0
    
    last_digit = number % 10
    remaining = number // 10
    
    if last_digit == digit:
        return 1 + count_digit(remaining, digit)
    else:
        return count_digit(remaining, digit)


def exercise_8():
    number = int(input("Ingrese un numero entero positivo: "))
    digit = int(input("Ingrese el digito a contar (0-9): "))
    
    count = count_digit(number, digit)
    print(f"\nEl digito {digit} aparece {count} veces en el numero {number}")


def main():
    while True:
        print("Seleccione un ejercicio (1-8) o '0' para salir:")
        option = input()
        
        if option == "0":
            break
        
        match option:
            case "1":
                exercise_1()
            case "2":
                exercise_2()
            case "3":
                exercise_3()
            case "4":
                exercise_4()
            case "5":
                exercise_5()
            case "6":
                exercise_6()
            case "7":
                exercise_7()
            case "8":
                exercise_8()
            case _:
                print("Opcion invalida. Intente de nuevo.")


if __name__ == "__main__":
    main()

