# recursividad.py

import os
import csv

import os
import csv
from programa import quitar_tildes

def leer_recursivo(ruta):
    datos = []
    for entrada in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, entrada)
        if os.path.isdir(ruta_completa):
            datos.extend(leer_recursivo(ruta_completa))
        elif entrada.endswith(".csv"):
            with open(ruta_completa, "r", encoding="utf-8") as archivo:
                reader = csv.DictReader(archivo)
                for fila in reader:
                    # Extraer niveles desde la ruta
                    partes = ruta_completa.split(os.sep)
                    try:
                        continente = quitar_tildes(partes[-4])
                        pais = quitar_tildes(partes[-3])
                        ciudad = quitar_tildes(os.path.splitext(partes[-1])[0])
                    except IndexError:
                        continente = pais = ciudad = "Desconocido"

                    # Agregar campos al ítem
                    fila["__ruta__"] = ruta_completa
                    fila["continente"] = continente
                    fila["pais"] = pais
                    fila["ciudad"] = ciudad
                    datos.append(fila)
    return datos