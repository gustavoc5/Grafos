# prim(matriz)
# Descrição: Obtém as arestas da árvore geradora mínima partir da matriz de adjacências de um grafo
# ponderado através do algoritmo de Prim.  Entrada: matriz de adjacências (tipo numpy.ndarray)  Saída: sequência de arestas correspondente a árvore geradora mínima (tipo List) e inteiro
# representando o custo da árvore geradora mínima (tipo Integer). Ex. [(0, 1), (1, 2)] 5

import numpy as np
import math


def prim(matriz):
    # Número de vértices no grafo
    n = len(matriz)
    # Dicionário para armazenar o custo mínimo de conexão de cada vértice à árvore geradora mínima
    custo = {}
    # Lista de todos os vértices no grafo
    V = list(np.arange(0, n))
    # Lista de vértices que foram adicionados à árvore geradora mínima
    S = []
    # Adicionar o vértice 0 à árvore geradora mínima como ponto de partida
    S.append(0)
    # Lista de vértices que ainda não foram adicionados à árvore geradora mínima
    N = []
    N.extend(V)
    N.remove(0)
    # Lista para armazenar as arestas selecionadas para a árvore geradora mínima
    T = []
    # Variável para armazenar o custo total das arestas na árvore geradora mínima
    total_cost = 0
    # Inicializar o custo de conexão de cada vértice à árvore geradora mínima como infinito, exceto para o vértice 0
    for i in range(n):
        if i != 0:
            custo[i] = math.inf
    # Loop principal do algoritmo de Prim
    while len(T) < n - 1:
        minn = math.inf
        x = 0
        y = 0
        # Loop para percorrer todos os pares possíveis de vértices onde um vértice está na árvore geradora mínima (S) e o outro não está (N)
        for v in S:
            for u in N:
                if matriz[v][u] and v != u:
                    if minn > matriz[v][u]:
                        minn = matriz[v][u]
                        x = v
                        y = u
        # Adicionar a aresta de menor peso à árvore geradora mínima e seu peso ao custo total
        T.append((x, y))
        total_cost += matriz[x][y]
        # Adicionar o vértice y à árvore geradora mínima e removê-lo da lista de vértices que ainda não estão na árvore
        S.append(y)
        N.remove(y)
    # Imprimir a árvore geradora mínima e seu custo total
    print(T, total_cost)
    return T, total_cost
