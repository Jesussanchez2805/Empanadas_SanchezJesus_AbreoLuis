from utils import cargar_empanadas, guardar_empanadas
from Agregar import agregar
from Editar import editar_empanada
from Eliminar import eliminar_empanada
from Listar import listar_empanadas

def menu():
    empanadas = cargar_empanadas()

    while True:
        print("\n--- MENU EMPANADAS ---")
        print("""1. AGREGAR EMPANADAS
2. LISTAR EMPANADAS
3. EDITAR EMPANADAS
4. ELIMINAR EMPANADAS
5. SALIR""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar()
        elif opcion == "2":
            listar_empanadas()
        elif opcion == "3":
            editar_empanada()
        elif opcion == "4":
            eliminar_empanada()
        elif opcion == "5":
            break
        else:
            print("Opción no válida")

menu()