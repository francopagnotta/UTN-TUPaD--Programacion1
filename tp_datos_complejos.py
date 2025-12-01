# Trabajo Practico 6: Estructuras de datos complejas
# Franco Pagnotta - Comision 5

# Ejercicio 1
def exercise_1():
    prices = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450}
    
    prices['Naranja'] = 1200
    prices['Manzana'] = 1500
    prices['Pera'] = 2300
    
    print("Diccionario actualizado:")
    for fruit, price in prices.items():
        print(f"{fruit}: {price}")
    
    return prices


# Ejercicio 2
def exercise_2():
    prices = exercise_1()
    
    prices['Banana'] = 1330
    prices['Manzana'] = 1700
    prices['Melon'] = 2800
    
    print("\nPrecios actualizados:")
    for fruit, price in prices.items():
        print(f"{fruit}: {price}")
    
    return prices


# Ejercicio 3
def exercise_3():
    prices = exercise_2()
    
    fruits_list = list(prices.keys())
    
    print("\nLista de frutas:")
    print(fruits_list)
    
    return fruits_list


# Ejercicio 4
def exercise_4():
    contacts = {}
    
    print("Ingrese 5 contactos:")
    for i in range(5):
        name = input(f"Ingrese el nombre del contacto {i + 1}: ")
        phone = input(f"Ingrese el numero telefonico de {name}: ")
        contacts[name] = phone
    
    search_name = input("\nIngrese el nombre del contacto a buscar: ")
    
    if search_name in contacts:
        print(f"El numero de {search_name} es: {contacts[search_name]}")
    else:
        print(f"No se encontro el contacto {search_name}")


# Ejercicio 5
def exercise_5():
    phrase = input("Ingrese una frase: ")
    
    words = phrase.lower().split()
    
    unique_words = set(words)
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    print("\nPalabras unicas:")
    print(unique_words)
    
    print("\nRecuento de palabras:")
    for word, count in word_count.items():
        print(f"{word}: {count}")


# Ejercicio 6
def exercise_6():
    students = {}
    
    print("Ingrese 3 alumnos con sus notas:")
    for i in range(3):
        name = input(f"Ingrese el nombre del alumno {i + 1}: ")
        
        notes = []
        for j in range(3):
            note = float(input(f"Ingrese la nota {j + 1} de {name}: "))
            notes.append(note)
        
        students[name] = tuple(notes)
    
    print("\nPromedios de los alumnos:")
    for name, notes in students.items():
        average = sum(notes) / len(notes)
        print(f"{name}: {average:.2f}")


# Ejercicio 7
def exercise_7():
    partial_1 = set()
    partial_2 = set()
    
    print("Ingrese estudiantes que aprobaron Parcial 1 (ingrese 'fin' para terminar):")
    while True:
        student = input("Nombre del estudiante: ")
        if student.lower() == 'fin':
            break
        partial_1.add(student)
    
    print("\nIngrese estudiantes que aprobaron Parcial 2 (ingrese 'fin' para terminar):")
    while True:
        student = input("Nombre del estudiante: ")
        if student.lower() == 'fin':
            break
        partial_2.add(student)
    
    both_partials = partial_1 & partial_2
    only_one = partial_1 ^ partial_2
    at_least_one = partial_1 | partial_2
    
    print("\nEstudiantes que aprobaron ambos parciales:")
    print(both_partials)
    
    print("\nEstudiantes que aprobaron solo uno de los dos:")
    print(only_one)
    
    print("\nLista total de estudiantes que aprobaron al menos un parcial:")
    print(at_least_one)


# Ejercicio 8
def exercise_8():
    products = {}
    
    while True:
        print("\nOpciones:")
        print("1. Consultar stock")
        print("2. Agregar unidades al stock")
        print("3. Agregar nuevo producto")
        print("4. Salir")
        
        option = input("Seleccione una opcion: ")
        
        if option == "1":
            product_name = input("Ingrese el nombre del producto: ")
            if product_name in products:
                print(f"Stock de {product_name}: {products[product_name]}")
            else:
                print(f"El producto {product_name} no existe")
        
        elif option == "2":
            product_name = input("Ingrese el nombre del producto: ")
            if product_name in products:
                units = int(input("Ingrese las unidades a agregar: "))
                products[product_name] += units
                print(f"Stock actualizado. Nuevo stock de {product_name}: {products[product_name]}")
            else:
                print(f"El producto {product_name} no existe")
        
        elif option == "3":
            product_name = input("Ingrese el nombre del nuevo producto: ")
            stock = int(input("Ingrese el stock inicial: "))
            products[product_name] = stock
            print(f"Producto {product_name} agregado con stock: {stock}")
        
        elif option == "4":
            break
        
        else:
            print("Opcion invalida")


# Ejercicio 9
def exercise_9():
    schedule = {}
    
    while True:
        print("\nOpciones:")
        print("1. Agregar evento")
        print("2. Consultar evento")
        print("3. Salir")
        
        option = input("Seleccione una opcion: ")
        
        if option == "1":
            day = input("Ingrese el dia: ")
            time = input("Ingrese la hora (formato HH:MM): ")
            event = input("Ingrese el evento: ")
            schedule[(day, time)] = event
            print("Evento agregado")
        
        elif option == "2":
            day = input("Ingrese el dia: ")
            time = input("Ingrese la hora (formato HH:MM): ")
            key = (day, time)
            
            if key in schedule:
                print(f"Evento: {schedule[key]}")
            else:
                print("No hay evento programado para ese dia y hora")
        
        elif option == "3":
            break
        
        else:
            print("Opcion invalida")


# Ejercicio 10
def exercise_10():
    original = {
        'argentina': 'buenos aires',
        'brasil': 'brasilia',
        'chile': 'santiago',
        'uruguay': 'montevideo'
    }
    
    inverted = {}
    for country, capital in original.items():
        inverted[capital] = country
    
    print("Diccionario original:")
    for country, capital in original.items():
        print(f"{country}: {capital}")
    
    print("\nDiccionario invertido:")
    for capital, country in inverted.items():
        print(f"{capital}: {country}")


def main():
    while True:
        print("Seleccione un ejercicio (1-10) o '0' para salir:")
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
            case "9":
                exercise_9()
            case "10":
                exercise_10()
            case _:
                print("Opcion invalida. Intente de nuevo.")


    main()

