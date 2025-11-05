import os
import unicodedata

def quitar_tildes(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def validar_dato(campo, tipo):
    while True:
        try:
            return tipo(input(f"{campo}: ").strip())
        except ValueError:
            print(f"Valor inválido para {campo}. Intente nuevamente.")

def obtener_ruta_csv(base_dir, niveles):
    return os.path.join(base_dir, *niveles) + ".csv"
