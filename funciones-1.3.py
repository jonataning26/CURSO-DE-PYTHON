#🧪 EJERCICIO 3 — DEFAULT ARGUMENTS

def calcular_descuento(precio, descuento=10):
    """
    descuento es porcentaje
    """
    total = precio-precio * descuento/100
    return total



    pass
salida = calcular_descuento(100)
print(f"cuenta con descuento final:{salida}","$")

salida = calcular_descuento(100,20)
print(f"cuenta con descuento final:{salida}","$")