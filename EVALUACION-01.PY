def clasificar_numero(n):
    """
    Retorna:
    - 'positivo par'
    - 'positivo impar'
    - 'negativo'
    - 'cero'
    """
    if n > 0:
        if n%2==0:
            return f"EL NUMERO {n} ES PAR"
        else:
            return f"EL NUMERO {n} ES IMPAR"
           
    elif n == 0:
        return f"EL NUMERO ES UN {n}"
    
    else:
        return f"EL NUMERO {n} ES UN NUMERO NEGATIVO"
    
ENTRADA = int(input("INGRESE EL NUEMERO A EVALUAR:"))
SALIDA =clasificar_numero(ENTRADA)
print("RESULTADOS DE LA EVALUACION:",SALIDA)
