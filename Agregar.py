from utils import guardar_empanadas, cargar_empanadas

def validar_cantidad():
    while True:
        try:
            cantidad = int(input("¿Cuántas empanadas desea registrar?: "))
            if cantidad <= 0:
                print("La cantidad debe ser un número entero positivo.")
            else:
                return cantidad
        except ValueError:
            print("Por favor ingrese un número entero.")

def validar_nombre():
    while True:
        nombre = input("Nombre: ")
        if nombre.strip() == "":
            print("El nombre no puede estar vacío.")
        else:
            return nombre
        
def validar_precio():
    while True:
        try:
            precio = float(input("Precio: "))
            if precio <= 0:
                print("El precio debe ser un número positivo.")
            else:
                return precio
        except ValueError:
            print("Por favor ingrese un número válido para el precio.")

def validar_ingredientes():
    while True:
        ingredientes = input("Ingredientes principales: ")
        if ingredientes.strip() == "":
            print("Los ingredientes no pueden estar vacíos.")
        else:
            return ingredientes

def validar_disponibilidad():
    while True:
        disponible = input("Disponible (si/no): ").lower()
        if disponible in ["si", "no"]:
            return disponible
        else:
            print("Por favor ingrese 'si' o 'no' para disponibilidad.")

from utils import guardar_empanadas, cargar_empanadas

def validar_cantidad():
    while True:
        try:
            cantidad = int(input("¿Cuántas empanadas desea registrar?: "))
            if cantidad <= 0:
                print("La cantidad debe ser un número entero positivo.")
            else:
                return cantidad
        except ValueError:
            print("Por favor ingrese un número entero.")

def validar_nombre():
    while True:
        nombre = input("Nombre: ")
        if nombre.strip() == "":
            print("El nombre no puede estar vacío.")
        else:
            return nombre
        
def validar_precio():
    while True:
        try:
            precio = float(input("Precio: "))
            if precio <= 0:
                print("El precio debe ser un número positivo.")
            else:
                return precio
        except ValueError:
            print("Por favor ingrese un número válido para el precio.")

def validar_ingredientes():
    while True:
        ingredientes = input("Ingredientes principales: ")
        if ingredientes.strip() == "":
            print("Los ingredientes no pueden estar vacíos.")
        else:
            return ingredientes

def validar_disponibilidad():
    while True:
        disponible = input("Disponible (si/no): ").lower()
        if disponible in ["si", "no"]:
            return disponible
        else:
            print("Por favor ingrese 'si' o 'no' para disponibilidad.")

def agregar():
    empanadas = cargar_empanadas()
    cantidad = validar_cantidad()

    for i in range(cantidad):
        print("\nRegistro de empanada", i + 1)

        nombre = validar_nombre()
        precio = validar_precio()
        ingredientes = validar_ingredientes()
        disponible = validar_disponibilidad()

        empanada = {
            "nombre": nombre,
            "precio": precio,
            "ingredientes": ingredientes,
            "disponible": disponible
        }

        empanadas.append(empanada)

    guardar_empanadas(empanadas)     
