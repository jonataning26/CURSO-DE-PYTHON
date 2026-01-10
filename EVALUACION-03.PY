def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: no se puede dividir entre cero"
    except TypeError:
        return "Error: ambos valores deben ser números"
print(dividir(10, 2))     # 5.0
print(dividir(10, 0))     # Error: no se puede dividir entre cero
print(dividir("a", 3))   # Error: ambos valores deben ser números
