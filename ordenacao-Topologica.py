# ordenacaoTopologica(listaAdj)
# Descrição: Obtém a ordenação topológica de um grafo acíclico direcionado.  Entrada: lista de adjacências (tipo Dictionary)  Saída: Lista com os índices dos vértices conforme ordem topológica (tipo List).


def ordenacaoTopologica(listaAdj, v=0):
    L = []
    cor = {v: "branco" for v in listaAdj}
    tempoD = {}
    tempoT = {}
    tempo = [0]
    total = {}

    def DFSaux(v):
        nonlocal tempo
        cor[v] = "cinza"
        tempo[0] += 1
        tempoD[v] = tempo[0]
        for u in listaAdj.get(v, []):
            if cor[u] == "branco":
                DFSaux(u)
        cor[v] = "preto"
        tempo[0] += 1
        tempoT[v] = tempo[0]
        L.append(v)

    DFSaux(v)

    for vert in listaAdj:
        if cor[vert] == "branco":
            DFSaux(vert)

    for vert in listaAdj.keys():
        total[vert] = f"{tempoD.get(vert, 0)}/{tempoT.get(vert, 0)}"

    L = list(reversed(L))

    msg = f"{total}\n{L}"

    print(msg)
    return msg
