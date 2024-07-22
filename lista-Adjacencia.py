import numpy as np


def lerInstancia(inst):
    # salva o caminho da instância na variável caminho_inst
    caminho_inst = "path" + inst + ".txt"
    # lê o conteúdo do arquivo da instância e armazena em uma matriz numpy
    mat = np.loadtxt(caminho_inst, dtype=int)
    return mat


def tipoGrafoLista(listaAdj):
    simples = True
    dirigido = False
    multigrafo = False
    pseudografo = False

    for vi in listaAdj:
        if len(listaAdj[vi]) != len(set(listaAdj[vi])):
            multigrafo = True
            simples = False
        for vj in listaAdj[vi]:
            if vi not in listaAdj[vj]:
                dirigido = True
                simples = False
            if vi == vj:
                pseudografo = True
                simples = False

    if pseudografo and dirigido:
        tipo = 31
    elif pseudografo:
        tipo = 30
    elif multigrafo and dirigido:
        tipo = 21
    elif multigrafo:
        tipo = 20
    elif dirigido:
        tipo = 1
    else:
        tipo = 0
    print(tipo)
    return tipo


def criaListaAdjacencias(matriz):
    vert = len(matriz)
    listaAdj = {}
    for vi in range(0, vert):
        adjc = []
        for vj in range(0, vert):
            aresta = matriz[vi][vj]
            if aresta > 0:
                for i in range(0, aresta):
                    adjc.append(vj)
        listaAdj[vi] = adjc
    print(listaAdj)
    return listaAdj


def verificaAdjacenciaLista(listaAdj, vi, vj):
    adjacencia = False
    if vj in listaAdj[vi]:
        adjacencia = True
    print(adjacencia)
    return adjacencia


def calcDensidadeLista(listaAdj):
    tipo = tipoGrafoLista(listaAdj)
    vert = len(listaAdj)
    arest = np.sum([len(vi) for vi in listaAdj.values()])
    if tipo == 0:
        densidade = arest / (vert * (vert - 1))
    else:
        densidade = (arest / 2) / (vert * (vert - 1))
    densidade = round(densidade, 3)
    print(densidade)
    return densidade


def insereArestaLista(listaAdj, vi, vj):
    if vi in listaAdj:
        listaAdj[vi].append(vj)
    else:
        listaAdj[vi] = [vj]
    if vj in listaAdj:
        listaAdj[vj].append(vi)
    else:
        listaAdj[vj] = [vi]
    print(listaAdj)
    return listaAdj


def removeArestaLista(listaAdj, vi, vj):
    if vi in listaAdj[vj]:
        listaAdj[vj].remove(vi)
    if vj in listaAdj[vi]:
        listaAdj[vi].remove(vj)
    print(listaAdj)
    return listaAdj


def insereVerticeLista(listaAdj, vi):
    if vi not in listaAdj:
        listaAdj[vi] = []
    print(listaAdj)
    return listaAdj


def removeVerticeLista(listaAdj, vi):
    if vi in listaAdj:
        for key in listaAdj:
            if vi in listaAdj[key]:
                while vi in listaAdj[key]:
                    listaAdj[key].remove(vi)
        del listaAdj[vi]
    print(listaAdj)
    return listaAdj


if __name__ == "__main__":
    caminho = "path"
    with open(caminho, "rb"):
        matriz = np.genfromtxt(caminho, dtype="int32")
    listaAdj = criaListaAdjacencias(matriz)

    tipoGrafoLista(listaAdj)

    verificaAdjacenciaLista(listaAdj, 2, 3)

    calcDensidadeLista(listaAdj)

    insereArestaLista(listaAdj, 0, 2)

    insereVerticeLista(listaAdj, 4)

    removeArestaLista(listaAdj, 3, 2)

    removeVerticeLista(listaAdj, 4)
