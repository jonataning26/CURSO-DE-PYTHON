def promedio(numeros):
    """
    Recibe una lista de números
    Retorna el promedio
    Si la lista está vacía o hay datos inválidos, retorna None
    """
    if numeros:
        promedio = 0
        for num in numeros:
            if isinstance(num,(int,float)):
                promedio += num
            else:
                return None
        return promedio /len(numeros)
                             
    else:
        return None
real = promedio([10, 20, 30, 40, 50])
if real is not None:
    print("promedio general:",real)
else:
    print(real)