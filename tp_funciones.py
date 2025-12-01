# Trabajo Practico - Funciones
# Franco Pagnotta - Comision 5

import math


# Ejercicio 1
def print_hello_world():
    print("Hola Mundo!")


# Ejercicio 2
def greet_user(name):
    return f"Hola {name}!"


# Ejercicio 3
def print_personal_info(name, last_name, age, residence):
    print(f"Soy {name} {last_name}, tengo {age} anos y vivo en {residence}")


# Ejercicio 4
def calculate_circle_area(radius):
    return math.pi * radius ** 2


def calculate_circle_perimeter(radius):
    return 2 * math.pi * radius


# Ejercicio 5
def seconds_to_hours(seconds):
    return seconds / 3600


# Ejercicio 6
def print_multiplication_table(number):
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")


# Ejercicio 7
def basic_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else None
    return (addition, subtraction, multiplication, division)


# Ejercicio 8
def calculate_imc(weight, height):
    return weight / (height ** 2)


# Ejercicio 9
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


# Ejercicio 10
def calculate_average(a, b, c):
    return (a + b + c) / 3


def print_circle_calculations():
    radius = float(input("Ingrese el radio del circulo: "))
    area = calculate_circle_area(radius)
    perimeter = calculate_circle_perimeter(radius)
    print(f"Area del circulo: {area:.2f}")
    print(f"Perimetro del circulo: {perimeter:.2f}")


def print_basic_operations():
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    results = basic_operations(a, b)
    print(f"Suma: {results[0]}")
    print(f"Resta: {results[1]}")
    print(f"Multiplicacion: {results[2]}")
    if results[3] is not None:
        print(f"Division: {results[3]}")
    else:
        print("Division: No se puede dividir por cero")


def run_exercise_2():
    name = input("Ingrese su nombre: ")
    print(greet_user(name))


def run_exercise_3():
    name = input("Ingrese su nombre: ")
    last_name = input("Ingrese su apellido: ")
    age = int(input("Ingrese su edad: "))
    residence = input("Ingrese su residencia: ")
    print_personal_info(name, last_name, age, residence)


def run_exercise_5():
    seconds = int(input("Ingrese los segundos: "))
    hours = seconds_to_hours(seconds)
    print(f"Horas: {hours:.2f}")


def run_exercise_6():
    number = int(input("Ingrese un numero: "))
    print_multiplication_table(number)


def run_exercise_8():
    weight = float(input("Ingrese su peso en kg: "))
    height = float(input("Ingrese su altura en metros: "))
    bmi = calculate_imc(weight, height)
    print(f"IMC: {bmi:.2f}")


def run_exercise_9():
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"Temperatura en Fahrenheit: {fahrenheit:.2f}")


def run_exercise_10():
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    c = float(input("Ingrese el tercer numero: "))
    average = calculate_average(a, b, c)
    print(f"Promedio: {average:.2f}")


def main():
    while True:
        print("\nSeleccione un ejercicio (1-10) o '0' para salir:")
        option = input()
        
        if option == "0":
            break
        
        print(f"\n--- Ejercicio {option} ---")
        match option:
            case "1":
                print_hello_world()
            case "2":
                run_exercise_2()
            case "3":
                run_exercise_3()
            case "4":
                print_circle_calculations()
            case "5":
                run_exercise_5()
            case "6":
                run_exercise_6()
            case "7":
                print_basic_operations()
            case "8":
                run_exercise_8()
            case "9":
                run_exercise_9()
            case "10":
                run_exercise_10()
            case _:
                print("Opcion invalida. Intente de nuevo.")


main()

