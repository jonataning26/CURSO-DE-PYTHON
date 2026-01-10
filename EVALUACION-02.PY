def contadorDeFrases(entrada):
    evaluacion = {}
    for i in entrada.split():
        i=i.lower().strip(";'][]><?!@#$%^&^&*()__==-~., ¿")
        if not i in evaluacion:
            evaluacion[i]=1
        else:
            evaluacion[i]+=1
    return evaluacion
salida = contadorDeFrases("Hola, hola! ¿hola? Python, python. PYTHON!")
print(salida)