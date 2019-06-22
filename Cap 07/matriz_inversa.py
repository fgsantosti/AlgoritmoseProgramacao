
#preenchendo diretamente a matriz m 3x4
m = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
#criando matriz vazia
mi = []
#imprime a matriz m
print(m)
#criando uma matriz vazia 4x3
for i in range(4):
    l = []
    for j in range(3):
        l.append(i)
    mi.append(l)
#passando as informações para da matriz m
#para matriz mi 
for i in range(4):
    for j in range(3):
        mi[i][j] = m[j][i]

#imprime a matriz transposta
print(mi)

