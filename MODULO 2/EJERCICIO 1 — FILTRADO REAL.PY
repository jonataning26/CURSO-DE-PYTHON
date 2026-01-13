usuarios = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 17},
    {"nombre": "Carlos", "edad": 35},
    {"nombre": "María", "edad": 29},
    {"nombre": "Pedro", "edad": "40"} 
]



def contar_mayores_de_edad(usuarios):
    if not isinstance(usuarios, list):
        return None

    mayores = 0

    for usuario in usuarios:
        if not isinstance(usuario, dict):
            continue

        edad = usuario.get("edad")

        try:
            edad = int(edad)
        except (ValueError, TypeError):
            continue

        if edad >= 18:
            mayores += 1

    return mayores
 
entrada_salida = contar_mayores_de_edad(usuarios)
print(entrada_salida)