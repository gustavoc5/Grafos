# kruskal(matriz)  Descrição: Obtém as arestas da árvore geradora mínima partir da matriz de adjacências de um grafo
# ponderado através do algoritmo de Kruskal.  Entrada: matriz de adjacências (tipo numpy.ndarray)  Saída: sequência de arestas correspondente a árvore geradora mínima (tipo List) e inteiro
# representando o custo da árvore geradora mínima (tipo Integer). Ex. [(0, 1), (1, 2)] 5


def kruskal(matriz):
    n = len(matriz)
    arestas = []
    for u in range(n):
        for v in range(n):
            if matriz[u][v]:
                arestas.append([u, v, matriz[u][v]])

    arestas.sort(key=lambda x: x[2])  # Ordenar as arestas por peso
    agm = []
    conjuntos = [{i} for i in range(n)]
    custoTotal = 0

    while len(agm) < (n - 1):
        for aresta in arestas:
            u, v, matriz[u][v] = aresta
            if len(conjuntos[u].intersection(conjuntos[v])) == 0:
                agm.append((u, v))
                conjuntos[u] = conjuntos[u].union(conjuntos[v])
                for w in conjuntos[v]:
                    conjuntos[w] = conjuntos[u]
                custoTotal += matriz[u][v]

    print(agm, custoTotal)
