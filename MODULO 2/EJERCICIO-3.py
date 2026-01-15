#vamos hacer un mini programa que calcule el total de la venta en esta lista que contiene diccionarios.
ventas = [
    {"producto": "Laptop", "precio": 1200, "cantidad": 1},
    {"producto": "Mouse", "precio": 20, "cantidad": 3},
    {"producto": "Teclado", "precio": "50", "cantidad": 2},
    {"producto": "Monitor", "precio": None, "cantidad": 1},
    {"producto": "USB", "precio": 10, "cantidad": "2"},
]
#ok vamos a crear una funcion que se encargue de recibir y procesar unicamente el calculo del total de la venta

def calcula_venta(venta):
    #hecho eso vamos a desempaquetar la lista y los diccionarios.
    total = 0
    for ventas in venta:
        try:
            precio = float(ventas.get("precio",0))
            cantidad = int(ventas.get("cantidad",0))
            total += precio * cantidad
        except (TypeError,ValueError,AttributeError):
            continue
    return total
salida = calcula_venta(ventas)
print(f"EL TOTAL DE LA COMPRA ES:{salida}")