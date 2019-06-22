''' Q2
Crie um programa que preencha uma matriz 2x4 com
números inteiros, calcule e mostre:
■ a quantidade de elementos entre 12 e 20 em cada linha;
■ a média dos elementos pares da matriz.

matriz = []
for i in range(2):
    linha = []
    for j in range(4):
        linha.append(int(input('Inserir: ')))
    print(linha)
    matriz.append(linha)
print(matriz)
'''
matriz = [[7, 4, 14, 1], [12, 13, 16, 4]]
cont = 0
soma_pares = 0
contp = 0
for i in range(2):
    for j in range(4):
        if(matriz[i][j]>12 and matriz[i][j]<20):
            cont +=1 #contando elementos entre 12 e 20
        if(matriz[i][j]%2==0):
          soma_pares = soma_pares + matriz[i][j]
          contp += 1
    print('Na linha ',i,'tem', cont, 'elementos entre 12 e 20')
    cont = 0 #zerando o cont 

media_pares = soma_pares/contp

print('A média dos elementos pares da matriz:', media_pares)
            
