from gestor_archivos import agregar_item
from gestor_archivos import mostrar_items
from gestor_archivos import modificar_item
from gestor_archivos import eliminar_item
from gestor_archivos import mostrar_estadisticas

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar nuevo ítem")
        print("2. Mostrar todos los ítems")
        print("3. Modificar un ítem")
        print("4. Eliminar un ítem")
        print("5. Estadísticas y ordenamiento")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_item()
        elif opcion == "2":
            mostrar_items()
        elif opcion == "3":
            modificar_item()
        elif opcion == "4":
            eliminar_item()
        elif opcion == "5":
            mostrar_estadisticas()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

#if __name__ == "__main__":
menu()
