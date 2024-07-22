# caminhoEuleriano(matriz)
# Descrição: Verifica se um grafo possui um caminho Euleriano.
# Entrada: matriz de adjacências (tipo numpy.ndarray)
# Saída: True se grafo possui caminho Euleriano, False caso contrário (Boolean)
import numpy as np


def caminhoEuleriano(matriz):
    n = np.shape(matriz)[0]
    total = 0
    i = 0
    while (total <= 2) and (i <= n - 1):
        grau = sum(matriz[i])
        if grau % 2 == 1:
            total += 1
        i += 1
    if total > 2:
        tipo = False
    else:
        tipo = True

    print(tipo)
    return tipo
