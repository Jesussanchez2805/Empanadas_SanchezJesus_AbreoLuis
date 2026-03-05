from utils import cargar_empanadas, guardar_empanadas

def editar_empanada(empanadas):
    nombre_buscar = input("Nombre de la empanada a editar: ")

    for e in empanadas:
        if e["nombre"].lower() == nombre_buscar.lower():
            print("Deje en blanco si no desea cambiar el valor.")

            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_precio = input("Nuevo precio: ")

            if nuevo_nombre != "":
                e["nombre"] = nuevo_nombre

            if nuevo_precio != "":
                e["precio"] = nuevo_precio

            guardar_empanadas(empanadas)
            print("Empanada actualizada.")
            return

    print("Empanada no encontrada.")