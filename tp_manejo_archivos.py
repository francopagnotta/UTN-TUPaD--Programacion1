# Trabajo Practico: Manejo de Archivos
# Franco Pagnotta - Comision 5

FILE_NAME = "productos.txt"


# Ejercicio 1
def exercise_1():
    products = [
        "Lapicera,120.5,30",
        "Cuaderno,350.0,15",
        "Regla,85.0,25"
    ]
    
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        for product in products:
            file.write(product + '\n')
    
    print(f"Archivo {FILE_NAME} creado exitosamente con 3 productos iniciales")


# Ejercicio 2
def exercise_2():
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    if not lines:
        print("El archivo esta vacio")
        return
    
    print("\nProductos en el archivo:")
    print("-" * 50) 
    
    for line in lines:
        line = line.strip()
        if line:
            parts = line.split(",")
            if len(parts) == 3:
                name = parts[0].strip()
                price = parts[1].strip()
                quantity = parts[2].strip()
                print(f"Producto: {name} | Precio: ${price} | Cantidad: {quantity}")


# Ejercicio 3
def exercise_3():
    name = input("Ingrese el nombre del producto: ")
    price = input("Ingrese el precio del producto: ")
    quantity = input("Ingrese la cantidad del producto: ")
    
    new_product = f"{name},{price},{quantity}\n"
    
    with open(FILE_NAME, 'a', encoding='utf-8') as file:
        file.write(new_product)
    
    print(f"Producto {name} agregado exitosamente al archivo")


# Ejercicio 4
def load_products():
    products = []
    
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    for line in lines:
        line = line.strip()
        if line:
            parts = line.split(",")
            if len(parts) == 3:
                product = {
                    'nombre': parts[0].strip(),
                    'precio': parts[1].strip(),
                    'cantidad': parts[2].strip()
                }
                products.append(product)
    
    return products


def exercise_4():
    products = load_products()
    
    if products:
        print(f"\nSe cargaron {len(products)} productos en la lista:")
        print("-" * 50)
        for i, product in enumerate(products, 1):
            print(f"{i}. {product}")
    else:
        print("No se pudieron cargar productos")


# Ejercicio 5
def exercise_5():
    products = load_products()
    
    if not products:
        return
    
    search_name = input("Ingrese el nombre del producto a buscar: ")
    
    found = False
    for product in products:
        if product['nombre'].lower() == search_name.lower():
            print("\nProducto encontrado:")
            print(f"Nombre: {product['nombre']}")
            print(f"Precio: ${product['precio']}")
            print(f"Cantidad: {product['cantidad']}")
            found = True
            break
    
    if not found:
        print(f"Error: No se encontro el producto '{search_name}'")


# Ejercicio 6
def save_products(products):
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        for product in products:
            line = f"{product['nombre']},{product['precio']},{product['cantidad']}\n"
            file.write(line)
    
    print(f"Se guardaron {len(products)} productos en el archivo")


def exercise_6():
    products = load_products()
    
    if not products:
        print("No hay productos para guardar")
        return
    
    save_products(products)


def exercise_complete():
    products = load_products()
    
    if not products:
        print("Creando archivo inicial...")
        exercise_1()
        products = load_products()
    
    while True:
        print("\n" + "=" * 50)
        print("Sistema de Gestion de Productos")
        print("=" * 50)
        print("1. Mostrar todos los productos")
        print("2. Agregar nuevo producto")
        print("3. Buscar producto por nombre")
        print("4. Guardar productos")
        print("5. Salir")
        
        option = input("\nSeleccione una opcion: ")
        
        if option == "1":
            print("\n--- Lista de Productos ---")
            for product in products:
                print(f"Producto: {product['nombre']} | Precio: ${product['precio']} | Cantidad: {product['cantidad']}")
        
        elif option == "2":
            name = input("Ingrese el nombre del producto: ")
            price = input("Ingrese el precio del producto: ")
            quantity = input("Ingrese la cantidad del producto: ")
            
            new_product = {
                'nombre': name,
                'precio': price,
                'cantidad': quantity
            }
            products.append(new_product)
            print(f"Producto {name} agregado a la lista")
        
        elif option == "3":
            search_name = input("Ingrese el nombre del producto a buscar: ")
            
            found = False
            for product in products:
                if product['nombre'].lower() == search_name.lower():
                    print("\nProducto encontrado:")
                    print(f"Nombre: {product['nombre']}")
                    print(f"Precio: ${product['precio']}")
                    print(f"Cantidad: {product['cantidad']}")
                    found = True
                    break
            
            if not found:
                print(f"Error: No se encontro el producto '{search_name}'")
        
        elif option == "4":
            save_products(products)
        
        elif option == "5":
            if products:
                save = input("Desea guardar los cambios antes de salir? (s/n): ")
                if save.lower() == 's':
                    save_products(products)
            print("Saliendo del programa...")
            break
        
        else:
            print("Opcion invalida. Intente de nuevo.")


def main():
    while True:
        print("Seleccione un ejercicio (1-6) o '7' para programa completo o '0' para salir:")
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
                exercise_complete()
            case _:
                print("Opcion invalida. Intente de nuevo.")


    main()


