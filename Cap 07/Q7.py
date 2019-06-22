''' Q7
Elabore um programa que preencha uma matriz M de ordem
6x4 e uma segunda matriz N de ordem 6x4, calcule
e imprima a soma das linhas de M com as colunas de N.
'''
'''
m = []
n = []
#criando a matriz m
for i in range(3):
    linha = []
    for j in range(2):
        linha.append(int(input()))
    m.append(linha)
#criando a matriz n
for i in range(3):
    linha = []
    for j in range(2):
        linha.append(int(input()))
    n.append(linha)
'''
m = [[6,4],[8,3],[7,2]]
n = [[10,5],[9,1],[11,0]]

soma_linha = 0
soma_coluna = 0
for i in range(3):
    soma_linha = 0
    for j in range(2):
        soma_linha = soma_linha + m[i][j]
    soma_f = 0
    for i in range(2):
        soma_coluna = 0
        for j in range(3):
            soma_coluna = soma_coluna + n[j][i]

        soma_f = soma_linha + soma_coluna
        print(soma_f)

