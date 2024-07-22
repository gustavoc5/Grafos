import numpy as np


def fordFulkerson(G, s, t):
    # Criar uma cópia da rede de fluxo original
    Gr = np.array(G, dtype=int)
    fluxoMaximo = 0
    caminhos_utilizados = []

    # Função auxiliar para encontrar um caminho de s para t na rede residual
    def encontrarCaminho(Gr, s, t):
        visitados = set()
        fila = [(s, [s])]
        while fila:
            (vertice, caminho_atual) = fila.pop(0)
            if vertice not in visitados:
                if vertice == t:
                    return caminho_atual
                visitados.add(vertice)
                for vizinho, capacidade in enumerate(Gr[vertice]):
                    if capacidade > 0:
                        fila.append((vizinho, caminho_atual + [vizinho]))
        return None

    while True:
        caminho = encontrarCaminho(Gr, s, t)
        if not caminho:
            break
        fluxoCaminho = min(Gr[u][v] for u, v in zip(caminho, caminho[1:]))
        for u, v in zip(caminho, caminho[1:]):
            Gr[u][v] -= fluxoCaminho
            Gr[v][u] += fluxoCaminho
        fluxoMaximo += fluxoCaminho
        caminhos_utilizados.append(caminho)

    return fluxoMaximo, caminhos_utilizados
