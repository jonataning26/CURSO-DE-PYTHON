#ejercicio 4
def es_par(numero):
    """
    Retorna True si es par, False si no
    """
    return  numero % 2 == 0
    
paridad = es_par(25651)
if paridad:
    print(f"el numero ingresado en la funcion es numero par por lo tanto es {paridad}")
else:
    print(f"el numero ingresado es impar por lo tanto es {paridad}")

#bonus extras

def clasificar_signo(n):
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "cero"
clasificador = clasificar_signo(-1)
print(f"el numero ingresado es:{clasificador}")