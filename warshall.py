# warshall(matriz)
# Descrição: Obtém a matriz de alcançabilidade de um grafo com base no algoritmo de Warshall.
# Entrada: matriz de adjacências (tipo numpy.ndarray)
# Saída: matriz de acessibilidade (tipo numpy.ndarray)
import numpy as np


def warshall(matriz):
    matriz = np.array(matriz)
    n = len(matriz)
    r = matriz
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if (r[i][j] == 1) or (r[i][k] == 1 and r[k][j] == 1):
                    r[i][j] = 1
                else:
                    r[i][j] = r[i][j]
    print(r)
    return r
