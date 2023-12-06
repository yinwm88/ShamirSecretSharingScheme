import random


def obtener_coeficientes_aleatorio(t, k):
    coeficientes = []
    numeros_unicos = random.sample(range(1, 100+1), t-1)
    for n in numeros_unicos:
        coeficientes.append(n)
    coeficientes.append(k)
    return coeficientes
