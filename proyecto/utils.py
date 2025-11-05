import os

def validar_dato(campo, tipo):
    while True:
        valor = input(f"{campo}: ").strip()
        try:
            valor = tipo(valor)
            if isinstance(valor, (int, float)) and valor <= 0:
                raise ValueError
            return valor
        except ValueError:
            print(f"Valor inválido para {campo}. Intente nuevamente.")

def obtener_ruta_csv(base, jerarquia):
    return os.path.join(base, *jerarquia) + ".csv"