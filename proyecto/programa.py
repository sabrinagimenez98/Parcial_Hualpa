import os
import csv
from recursividad import leer_recursivo
from utiles import validar_dato, obtener_ruta_csv, quitar_tildes

BASE_DIR = "datos"

def agregar_item():
    continente = quitar_tildes(input("Continente: ").strip().title())
    pais = quitar_tildes(input("País: ").strip().title())
    ciudad = quitar_tildes(input("Ciudad: ").strip().title())
    nombre = quitar_tildes(input("Nombre de la ciudad: ").strip().title())
    poblacion = validar_dato("Población", int)
    superficie = validar_dato("Superficie (km2)", float)

    ruta_csv = obtener_ruta_csv(BASE_DIR, [continente, pais, ciudad])
    os.makedirs(os.path.dirname(ruta_csv), exist_ok=True)

    with open(ruta_csv, "a", newline='', encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie"])
        if archivo.tell() == 0:
            writer.writeheader()
        writer.writerow({"nombre": nombre, "poblacion": poblacion, "superficie": superficie})
    print("Ítem agregado exitosamente.")

def mostrar_items():
    items = leer_recursivo(BASE_DIR)
    # Ordenar por país y ciudad sin tildes
    items.sort(key=lambda i: (quitar_tildes(i["pais"]), quitar_tildes(i["ciudad"])))
    for item in items:
        nombre = quitar_tildes(item["nombre"])
        continente = item["continente"]
        pais = item["pais"]
        ciudad = item["ciudad"]
        poblacion = item["poblacion"]
        superficie = item["superficie"]
        print(f"{nombre} - {ciudad}, {pais} ({continente}) | Población: {poblacion}, Superficie: {superficie} km²")

def modificar_item():
    items = leer_recursivo(BASE_DIR)
    nombre = quitar_tildes(input("Nombre exacto del ítem a modificar: ").strip())
    encontrados = [i for i in items if quitar_tildes(i["nombre"]) == nombre]

    if not encontrados:
        print("Ítem no encontrado.")
        return

    item = encontrados[0]
    print(f"Ítem encontrado: {item}")
    campo = input("¿Qué campo desea modificar? (nombre/poblacion/superficie): ").strip()
    if campo not in item:
        print("Campo inválido.")
        return

    nuevo_valor = validar_dato(f"Nuevo valor para {campo}", int if campo == "poblacion" else float if campo == "superficie" else str)
    if campo == "nombre":
        nuevo_valor = quitar_tildes(nuevo_valor.strip().title())
    item[campo] = nuevo_valor

    ruta_csv = item["__ruta__"]
    with open(ruta_csv, "r", encoding="latin-1") as archivo:
        reader = list(csv.DictReader(archivo))
    for fila in reader:
        if quitar_tildes(fila["nombre"]) == nombre:
            fila[campo] = str(nuevo_valor)
            break

    with open(ruta_csv, "w", newline='', encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie"])
        writer.writeheader()
        writer.writerows(reader)
    print("Ítem modificado con éxito.")

def eliminar_item():
    items = leer_recursivo(BASE_DIR)
    nombre = quitar_tildes(input("Nombre exacto del ítem a eliminar: ").strip())
    encontrados = [i for i in items if quitar_tildes(i["nombre"]) == nombre]

    if not encontrados:
        print("Ítem no encontrado.")
        return

    item = encontrados[0]
    ruta_csv = item["__ruta__"]

    with open(ruta_csv, "r", encoding="latin-1") as archivo:
        reader = list(csv.DictReader(archivo))
    reader = [fila for fila in reader if quitar_tildes(fila["nombre"]) != nombre]

    with open(ruta_csv, "w", newline='', encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie"])
        writer.writeheader()
        writer.writerows(reader)
    print("Ítem eliminado con éxito.")

def mostrar_estadisticas():
    items = leer_recursivo(BASE_DIR)
    total = len(items)
    suma_poblacion = sum(int(i["poblacion"]) for i in items)
    promedio = suma_poblacion / total if total else 0
    print(f"Total de ítems: {total}")
    print(f"Población total: {suma_poblacion}")
    print(f"Población promedio: {promedio:.2f}")

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

menu()