def dividir(a, b):
    """
    Retorna a / b
    Si b es 0, retorna None
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None
salida = dividir(10,10)
if salida is not None:
    print(f"el resultado de la division es:{salida}")
else:
    print(f"math error!!!")