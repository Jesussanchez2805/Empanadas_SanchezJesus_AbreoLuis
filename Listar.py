from utils import cargar_empanadas

def listar_empanadas():
    empanadas = cargar_empanadas()

    if not empanadas:
        print("No hay empanadas registradas.")
        return

    print("\n*** EMPANADAS REGISTRADAS ***")

    for i, e in enumerate(empanadas, 1):

        print(f"\nEmpanada {i}")
        print(f"Nombre: {e['nombre']}")
        print(f"Precio: {e['precio']}")
        print(f"Ingredientes: {e['ingredientes']}")
        print(f"Estado: {e['disponible']}")

listar_empanadas()