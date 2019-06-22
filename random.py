  
import random

lista = []
for i in range(41):
    a = random.randint(1, 7)
    lista.append(a)

for i in range(41):
    print(i ,' - ',lista[i])

