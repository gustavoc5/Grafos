# floydWarshall(matriz)
# Descrição:  Obtém  a  matriz de custos  mínimos  de um grafo  a partir da matriz  de adjacências  de
# um grafo ponderado através do algoritmo de Floyd-Warshall.  Entrada: matriz de adjacências (tipo numpy.ndarray)  Saída: matriz de custos mínimos (tipo numpy.ndarray)
import numpy as np
import math


def floydWarshall(matriz):
    n = len(matriz)
    dist = np.array(matriz, dtype=float)
    dist[dist == -1] = math.inf
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    dist = np.array(dist, dtype=int)
    np.fill_diagonal(dist, 0)
    return print(dist.tolist())
