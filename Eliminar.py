from utils import cargar_empanadas, guardar_empanadas

def eliminar_empanada(empanadas):
    nombre_buscar = input("Nombre de la empanada a eliminar: ")

    for e in empanadas:
        if e["nombre"].lower() == nombre_buscar.lower():
            empanadas.remove(e)
            guardar_empanadas(empanadas)
            print("Empanada eliminada.")
            return

    print("Empanada no encontrada.")