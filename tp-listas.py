# Trabajo Practico - Listas
# Franco Pagnotta - Comision 5

import random


# Ejercicio 1
def calculate_student_grades():
    grades = [85, 92, 78, 96, 88, 75, 90, 83, 79, 87]
    
    print("Lista completa de notas:")
    for grade in grades:
        print(grade)
    
    average = sum(grades) / len(grades)
    print(f"\nPromedio: {average:.2f}")
    print(f"Nota mas alta: {max(grades)}")
    print(f"Nota mas baja: {min(grades)}")


# Ejercicio 2
def manage_product_list():
    products = []
    
    for i in range(5):
        product = input(f"Ingrese el producto {i + 1}: ")
        products.append(product)
    
    sorted_products = sorted(products)
    print("\nLista ordenada alfabeticamente:")
    for product in sorted_products:
        print(product)
    
    product_to_remove = input("\nQue producto desea eliminar? ")
    if product_to_remove in products:
        products.remove(product_to_remove)
        print("\nLista actualizada:")
        for product in products:
            print(product)
    else:
        print("El producto no se encuentra en la lista.")


# Ejercicio 3
def get_even_and_odd_numbers():
    numbers = [random.randint(1, 100) for _ in range(15)]
    even_numbers = []
    odd_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    print("Lista completa:")
    
    for num in numbers:
        print(num)
    
    print(f"\nCantidad de numeros pares: {len(even_numbers)}")
    print(f"Cantidad de numeros impares: {len(odd_numbers)}")


# Ejercicio 4
def remove_duplicate_elements():
    original_list = [1, 2, 3, 2, 4, 3, 5, 1, 6, 4, 7, 2]
    
    unique_list = []
    for item in original_list:
        if item not in unique_list:
            unique_list.append(item)
    
    print("Lista original:")
    for item in original_list:
        print(item)
    
    print("\nLista sin elementos repetidos:")
    for item in unique_list:
        print(item)


# Ejercicio 5
def manage_student_list():
    students = ["Juan", "Maria", "Pedro", "Ana", "Luis", "Laura", "Carlos", "Sofia"]
    
    print("Lista de estudiantes:")
    for i, student in enumerate(students, 1):
        print(f"{i}. {student}")
    
    action = input("\nDesea agregar (a) o eliminar (e) un estudiante? ")
    
    if action.lower() == "a":
        new_student = input("Ingrese el nombre del nuevo estudiante: ")
        students.append(new_student)
    elif action.lower() == "e":
        student_to_remove = input("Ingrese el nombre del estudiante a eliminar: ")
        if student_to_remove in students:
            students.remove(student_to_remove)
        else:
            print("El estudiante no se encuentra en la lista.")
    
    print("\nLista final actualizada:")
    for i, student in enumerate(students, 1):
        print(f"{i}. {student}")


# Ejercicio 6
def rotate_list_right():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    
    print("Lista original:")
    for num in numbers:
        print(num)
    
    last_element = numbers.pop()
    numbers.insert(0, last_element)
    
    print("\nLista rotada una posicion a la derecha:")
    for num in numbers:
        print(num)


# Ejercicio 7
def get_weekly_temperatures():
    temperatures = [
        [15, 25],
        [12, 22],
        [18, 28],
        [14, 24],
        [16, 26],
        [13, 23],
        [17, 27]
    ]
    
    min_temperatures = []
    max_temperatures = []

    for day in temperatures:
        min_temperatures.append(day[0])
        max_temperatures.append(day[1])
    
    average_min_temperature = sum(min_temperatures) / len(min_temperatures)
    average_max_temperature = sum(max_temperatures) / len(max_temperatures)
    
    print(f"Promedio de temperaturas minimas: {average_min_temperature:.2f}")
    print(f"Promedio de temperaturas maximas: {average_max_temperature:.2f}")
    
    amplitudes = [max_temperatures[i] - min_temperatures[i] for i in range(7)]
    max_amplitude_day = amplitudes.index(max(amplitudes)) + 1
    
    print(f"El dia {max_amplitude_day} registro la mayor amplitud termica: {max(amplitudes)} grados")


# Ejercicio 8
def calculate_average_by_student_and_subject():
    grades = [
        [85, 90, 88],
        [78, 82, 80],
        [92, 95, 90],
        [75, 78, 76],
        [88, 85, 87]
    ]
    
    print("Promedio de cada estudiante:")
    for i, student_grades in enumerate(grades, 1):
        average = sum(student_grades) / len(student_grades)

        print(f"Estudiante {i}: {average:.2f}")
    
    print("\nPromedio de cada materia:")

    num_subjects = len(grades[0])

    for j in range(num_subjects):
        subject_grades = []
        for i in range(len(grades)):
            subject_grades.append(grades[i][j])
   
        average = sum(subject_grades) / len(subject_grades)
        
        print(f"Materia {j + 1}: {average:.2f}")


# Ejercicio 9
def play_tic_tac_toe():
    board = [["-" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    def display_board():
        for row in board:
            for cell in row:
                print(cell, end=" ")
            print()
    
    print("Tablero inicial:")
    
    display_board()
    
    for move in range(9):
        print(f"\nTurno del jugador {current_player}")
        row = int(input("Ingrese la fila (0-2): "))
        col = int(input("Ingrese la columna (0-2): "))
        
        if board[row][col] == "-":
            board[row][col] = current_player
            display_board()
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Esa casilla ya esta ocupada. Intente de nuevo.")
            move -= 1


# Ejercicio 10
def get_product_sales():
    sales = [
        [10, 15, 12, 18, 20, 14, 16],
        [8, 12, 10, 15, 18, 11, 13],
        [20, 25, 22, 28, 30, 24, 26],
        [5, 8, 6, 10, 12, 7, 9]
    ]
    
    print("Total vendido por cada producto:")

    for i, product_sales in enumerate(sales, 1):
        total = sum(product_sales)

        print(f"Producto {i}: {total}")
    
    daily_total = []

    for j in range(7):
        day_sum = 0
        for i in range(4):
            day_sum += sales[i][j]
        daily_total.append(day_sum)
    
    max_sales_day = daily_total.index(max(daily_total)) + 1

    print(f"\nEl dia {max_sales_day} tuvo las mayores ventas totales: {max(daily_total)}")
    
    product_totals = []

    for product_sales in sales:
        product_totals.append(sum(product_sales))

    most_sold_product = product_totals.index(max(product_totals)) + 1

    print(f"El producto mas vendido en la semana fue el producto {most_sold_product} con {max(product_totals)} unidades")


def main():
    menu_options = {
        "1": calculate_student_grades,
        "2": manage_product_list,
        "3": get_even_and_odd_numbers,
        "4": remove_duplicate_elements,
        "5": manage_student_list,
        "6": rotate_list_right,
        "7": get_weekly_temperatures,
        "8": calculate_average_by_student_and_subject,
        "9": play_tic_tac_toe,
        "10": get_product_sales
    }
    
    while True:
        print("\nSeleccione un ejercicio (1-10) o '0' para salir:")
        option = input()
        
        if option == "0":
            break
        elif option in menu_options:
            print(f"\n--- Ejercicio {option} ---")
            menu_options[option]()
        else:
            print("Opcion invalida. Intente de nuevo.")



main()

