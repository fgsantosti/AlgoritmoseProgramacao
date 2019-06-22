'''
Funcao split()
'''

frase = "um tigre, dois tigres, três tigres"
l = list(frase)
print(l)

for i in range(len(l)):
    if(l[i] == ","):
        l[i] = " "

print(l)

s = "".join(l)

print(s.split())


    
