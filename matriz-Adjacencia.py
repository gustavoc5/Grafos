import numpy as np
import sys


def lerInstancia(inst):
    # salva o caminho da instância na variável caminho_inst
    caminho_inst = "path" + inst + ".txt"
    # lê o conteúdo do arquivo da instância e armazena em uma matriz numpy
    mat = np.loadtxt(caminho_inst, dtype=int)
    return mat


def tipoGrafo(matriz):
    laco = False
    multipla = False
    vert = len(matriz)
    for i in range(vert):
        for j in range(vert):
            if matriz[i][j] > 1:
                multipla = True
            if matriz[i][j] > 0 and i == j:
                laco = True
    if (np.transpose(matriz) == matriz).all():
        dirigido = False
    else:
        dirigido = True
    if dirigido and multipla and laco:
        tipo = 31
    elif dirigido and multipla:
        tipo = 21
    elif dirigido:
        tipo = 1
    elif laco:
        tipo = 30
    elif multipla:
        tipo = 20
    else:
        tipo = 0
    print(tipo)
    return tipo


def verificaAdjacencia(matriz, vi, vj):
    adjacencia = False
    if matriz[vi][vj] > 0:
        adjacencia = True
    print(adjacencia)
    return adjacencia


def calcDensidade(matriz):
    vert = len(matriz)
    if (np.transpose(matriz) == matriz).all():
        arest = np.sum(matriz) / 2
        densidade = 2 * arest / (vert * (vert - 1))
    else:
        arest = np.sum(matriz)
        densidade = arest / (vert * (vert - 1))
    densidade = round(densidade, 3)
    print(densidade)
    return densidade


def insereAresta(matriz, vi, vj):
    matriz[vi][vj] += 1
    matriz[vj][vi] += 1
    print(matriz)
    return matriz


def insereVertice(matriz):
    vert = len(matriz)
    nova_matriz = np.zeros((vert + 1, vert + 1), dtype=int)
    nova_matriz[:vert, :vert] = matriz
    print(nova_matriz)
    return nova_matriz


def removeAresta(matriz, vi, vj):
    if matriz[vi][vj] > 0 and matriz[vj][vi] > 0:
        matriz[vi][vj] -= 1
        matriz[vj][vi] -= 1
    elif matriz[vi][vj] > 0:
        matriz[vi][vj] -= 1
    elif matriz[vj][vi] > 0:
        matriz[vi][vj] -= 1
    else:
        matriz[vi][vj] = matriz[vj][vi] = 0
    print(matriz)
    return matriz


def removeVertice(matriz, vi):
    vert = len(matriz)
    for linha in range(vert):
        for coluna in range(vert):
            if linha == vi or coluna == vi:
                matriz[linha][coluna] = -1
    matriz = np.array(matriz)
    print(matriz)
    return matriz


if __name__ == "__main__":
    # obtém o nome da instância a partir do argumento passado na linha de comando
    # inst = sys.argv[1]

    # # lê a instância e obtém suas dimensões
    # matriz = lerInstancia(inst)

    # tipoGrafo(matriz)
    tipoGrafo([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])
    tipoGrafo([[0, 2, 2, 1], [2, 0, 0, 1], [2, 0, 0, 1], [1, 1, 1, 0]])
    tipoGrafo([[0, 0, 0, 0], [1, 0, 1, 0], [0, 0, 0, 1], [0, 1, 0, 0]])
    tipoGrafo([[0, 2, 0, 0], [2, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])
    tipoGrafo([[0, 0, 0, 0], [2, 0, 1, 0], [0, 0, 0, 1], [0, 1, 0, 0]])
    tipoGrafo([[1, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 1]])
    tipoGrafo([[1, 0, 0, 0], [1, 0, 1, 0], [0, 0, 0, 1], [0, 1, 0, 1]])
