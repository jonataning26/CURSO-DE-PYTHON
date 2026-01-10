"""Reglas

❌ No input()

❌ No print() dentro de la función

✅ Solo lógica y return
"""
    
while True:
    edad_de_persona = input("INGRESE TU EDAD:")
    try:
        if  edad_de_persona.strip():
            if edad_de_persona.isnumeric():
                edad_de_persona=int(edad_de_persona)
                if edad_de_persona > 0:
                    break
                else:
                    print("error evite que el campo edad sea un 0 o un numero negativo!!!")
            else:
                print("error campo edad no puede ser un texto!!!")
        else:
            print("error el campo de entrada no puede estar vacio!!!.")
    except ValueError:
        pass

def clasificar_edad(edad):
    if edad < 18:
        return "menor de edad"
    elif edad >=18 and edad<= 30 :
        return "mayor de edad"
    elif edad > 30 and edad <= 100:
        return "adulto mayor"
    else:
        return " la edad esta fuera de rango" 
salida=clasificar_edad(edad_de_persona)
print(f"la persona es:{salida}")

