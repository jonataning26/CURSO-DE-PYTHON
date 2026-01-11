def analizar_numeros(lista):
    """
    Recibe una lista de números
    Retorna un diccionario con:
    - 'pares'
    - 'impares'
    - 'suma'
    """
    evaluacion_final= {"pares":0,"impares":0,"suma":0}
    for tester in lista:       
        if tester % 2 == 0:
            evaluacion_final["pares"]+=1
            evaluacion_final["suma"]+=tester
        else:
            evaluacion_final["impares"]+=1
            evaluacion_final["suma"]+=tester
    return evaluacion_final

numeros = [12, 7, 5, 8, 3, 10, 15, 2, 9]
analista = analizar_numeros(numeros)
print(analista)