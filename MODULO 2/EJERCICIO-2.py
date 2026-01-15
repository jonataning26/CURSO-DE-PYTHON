productos = [
    {"nombre": "Laptop", "precio": 1200},
    {"nombre": "Mouse", "precio": 20},
    {"nombre": "Teclado", "precio": "50"},   # string numérico
    {"nombre": "Monitor", "precio": None},   # inválido
    {"nombre": "USB", "precio": 10}
]
def total_precio(productos):
    """
    Recibe una lista de diccionarios con clave 'precio'
    Retorna la suma total de los precios válidos
    Ignora precios inválidos
    """
    suma = {"total": 0}
    for item in productos:
        if not isinstance(item,dict) or len(item) == 0:
            continue
        try:
            precio = item.get("precio")
            precio=float(precio)
            suma["total"]+=precio
        except (TypeError,ValueError):
            pass
    return suma
salida = total_precio(productos)
print(salida)