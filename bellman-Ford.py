# bellmanFord(matriz, vOrigem, vDestino)
# Descrição:  Obtém  o  caminho  mínimo  entre  um  vértice  origem  (vOrigem)  e  um  vértice  destino
# (vDestino)  a  partir  da  matriz  de  adjacências  de  um  grafo  ponderado  através  do
# algoritmo de Bellman-Ford.  Entrada: matriz de adjacências (tipo numpy.ndarray)  Saída: False caso o grafo possua ciclos de custo negativo. Caso contrário, sequência de vértices
# correspondente ao caminho mínimo (tipo List) e inteiro representando o custo do caminho
# (tipo Integer). Ex. [0, 1, 2, 3] 5
import numpy as np
import math


def bellmanFord(matriz, vOrigem, vDestino):
    n = len(matriz)
    dist = np.array(matriz, dtype=float)
    np.fill_diagonal(dist, 0)
    dist[dist == -1] = math.inf
    custo = {}
    rota = {}
    for i in range(n):
        custo[i] = math.inf
        rota[i] = []
    custo[vOrigem] = 0
    vert = list(np.arange(0, n))
    for i in range(len(vert) - 1):
        for v in vert:
            for u in vert:
                if dist[v][u] != 0 and custo[v] != math.inf:
                    if custo[u] > (custo[v] + dist[v][u]):
                        custo[u] = custo[v] + dist[v][u]
                        rota[u] = rota[v] + [v]
    for v in vert:
        for u in vert:
            if dist[v][u] != 0 and custo[u] > (custo[v] + dist[v][u]):
                return print(False)
    return print(rota[vDestino] + [vDestino], int(custo[vDestino]))
