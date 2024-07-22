# DFS(listaAdj)- Recursivo
# Descrição:  Busca  em profundidade de  um grafo utilizando estratégia  recursiva.  Retorna  a
# sequência dos vértices visitados.  Entrada: lista de adjacências (tipo Dictionary)  Saída: sequência de vértices (tipo List)


def DFS(listaAdj, v=0):
    visitado = []

    def DFS_recursiva(v):
        visitado.append(v)
        for vert in listaAdj[v]:
            if vert not in visitado:
                DFS_recursiva(vert)

    DFS_recursiva(v)
    x = listaAdj.keys()
    for vert in x:
        if vert not in visitado:
            visitado.append(vert)

    print(visitado)
    return visitado
