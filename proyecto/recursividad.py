# recursividad.py

import os
import csv

def leer_recursivo(ruta):
    datos = []
    for entrada in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, entrada)
        if os.path.isdir(ruta_completa):
            datos.extend(leer_recursivo(ruta_completa))
        elif entrada.endswith(".csv"):
            with open(ruta_completa, "r") as archivo:
                reader = csv.DictReader(archivo)
                for fila in reader:
                    fila["__ruta__"] = ruta_completa
                    datos.append(fila)
    return datos