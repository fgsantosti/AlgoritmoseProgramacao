#pegar a distância
distancia = float(input())



if(distancia >0 and distancia <= 200):
    op1 = distancia * 0.50
    print(op1)
elif(distancia > 200):
    op2 = distancia * 0.45
    print(op2)
else:
    print('Possivelmente o valor é negativo.')
    
