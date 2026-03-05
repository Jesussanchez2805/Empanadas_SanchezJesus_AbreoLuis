from utils import cargar_empanadas, guardar_empanadas

def eliminar_empanada(empanadas):
    nombre_buscar = input("Nombre de la empanada a eliminar: ")
    
    if not empanadas:
        print("  El catálogo está vacío. ¡Agrega tu primera empanada!")
        return

    for e in empanadas:
        if e["nombre"].lower() == nombre_buscar.lower():
            empanadas.remove(e)
            guardar_empanadas(empanadas)
            print("Empanada eliminada.")
            return