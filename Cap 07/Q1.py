''' Q1 
Faça um programa que preencha uma matriz 3x5 com
números inteiros, calcule e mostre a quantidade de
elementos entre 15 e 20.'''

matriz = []

#a quantidade de linhas da matriz
for i in range(3):
    linha = []
    #a quantidade de colunas da matriz
    for j in range(5):
        linha.append(int(input('Inserir número inteiro:')))
    #print(linha)#imprimo a linha completa
    #inserindo a linha na matriz
    matriz.append(linha)
#print(matriz) #imprime a matriz completa
cont = 0
#matriz = [[8, 5, 2, 18, 4], [9, 6, 3, 7, 4], [7, 4, 1, 2, 3]]
for i in range(3):
    for j in range(5):
        if (matriz[i][j]>15) and (matriz[i][j]<20):
            print('=> ',matriz[i][j])
            cont += 1 #cont = cont + 1
            
print('A quantidade de elementos entre 15 e 20:', cont)
