from utils import guardar_empanadas

def agregar():
    cantidad = int(input("¿Cuántas empanadas desea registrar?: "))

    for i in range(cantidad):
        print("\nRegistro de empanada", i + 1)

        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        ingredientes = input("Ingredientes principales: ")
        disponible = input("Disponible (si/no): ")

        empanada = {
            "nombre": nombre,
            "precio": precio,
            "ingredientes": ingredientes,
            "disponible": disponible
        }
    guardar_empanadas(empanada)    
