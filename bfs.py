# BFS(listaAdj)
# Descrição: Busca em largura de um grafo retornando a sequência dos vértices visitados.  Entrada: lista de adjacências (tipo Dictionary)  Saída: sequência de vértices (tipo List)


def BFS(listaAdj, v=0):
    q = []
    q.append(v)
    analisado = []
    while q:
        v = q.pop(0)
        for vert in listaAdj[v]:
            if vert not in analisado and vert not in q:
                q.append(vert)
        analisado.append(v)

    x = listaAdj.keys()
    for vert in x:
        if vert not in analisado:
            analisado.append(vert)
    print(analisado)
    return analisado
