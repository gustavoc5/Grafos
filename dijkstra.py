# dijkstra(matriz, vOrigem, vDestino)
# Descrição:  Obtém  o  caminho  mínimo  entre  um  vértice  origem  (vOrigem)  e  um  vértice  destino
# (vDestino)  a  partir  da  matriz  de  adjacências  de  um  grafo  ponderado  através  do
# algoritmo de Dijkistra.  Entrada: matriz de adjacências (tipo numpy.ndarray)  Saída: sequência de vértices correspondente ao caminho mínimo (tipo List) e inteiro
# representando o custo do caminho (tipo Integer). Ex. [0, 1, 2, 3] 5
import numpy as np
import math


def dijkstra(matriz, vOrigem, vDestino):
    n = len(matriz)
    dist = np.array(matriz, dtype=float)
    np.fill_diagonal(dist, 0)
    dist[dist == -1] = math.inf
    custo = {}
    rota = {}
    custo[vOrigem] = 0
    rota[vOrigem] = [vOrigem]
    for i in range(n):
        if i != vOrigem:
            custo[i] = math.inf
            rota[i] = []
    A = list(np.arange(0, n))
    F = []
    while A:
        v = min(A, key=custo.get)
        F.append(v)
        A.remove(v)
        N = []
        for i in range(len(dist[v])):
            if dist[v][i] != 0 and dist[v][i] != math.inf:
                N.append(i)
        N = list(set(N) - set(F))
        for u in N:
            if custo[v] + dist[v][u] < custo[u]:
                custo[u] = custo[v] + dist[v][u]
                rota[u] = rota[v] + [u]

    return print(rota[vDestino], int(custo[vDestino]))
