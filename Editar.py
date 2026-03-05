from utils import cargar_empanadas, guardar_empanadas

def editar_empanada():
    empanadas = cargar_empanadas()
    nombre_buscar = input("Nombre de la empanada a editar: ")

    if not empanadas:
        print("  El catálogo está vacío. ¡Agrega tu primera empanada!")
        return
    
    for e in empanadas:
        if e["nombre"].lower() == nombre_buscar.lower():
            print("Deje en blanco si no desea cambiar el valor.")

            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_precio = float(input("Nuevo precio: "))
            nuevo_ingredientes = input("Nuevos ingredientes")
            nuevo_disponible = input("Estado de las empanadas disponible (si/no)")

            if nuevo_nombre != "":
                e["nombre"] = nuevo_nombre

            if nuevo_precio != "":
                e["precio"] = nuevo_precio
            if nuevo_ingredientes != "":
                e["ingredientes"] = nuevo_ingredientes
            if nuevo_disponible != "":
                e["disponible"] = nuevo_disponible
                
            guardar_empanadas(empanadas)
            print("Empanada actualizada.")
            return