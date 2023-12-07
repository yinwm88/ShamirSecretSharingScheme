def algoritmo_horner(x, coeficientes):
    y = 0
    for  coeficiente in coeficientes:
        y = (y * x) + coeficiente
    return y
