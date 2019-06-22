
lista1 = [87,5,7,3,6,7,2,10]

lista2 = [87,7,6,5,2,7,8,20]

lista3 = []

existe = False 

for i in range(len(lista1)):
    existe = False 
    for j in range(len(lista2)):
        if(lista2[i] == lista1[j]):
            existe = True

    if(existe == False):
        lista1.append(lista2[i])

#
for i in range(len(lista1)):
    lista3.append(lista1[i])

print(lista3)       

existe1 = False 
cont = 0
posicao = 0
lista4 = []
for i in range(len(lista3)):
    cont = 0
    posicao = 0
    for j in range(len(lista3)):
        if(lista3[i] == lista3[j]):
            cont = cont + 1

    if(cont == 1):
        lista4.append(lista3[i])

    if(cont == 2):
        posicao = i
    
    lista3[posicao] = 0

print(lista4)  

