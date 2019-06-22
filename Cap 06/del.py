

nomes_telefones = [["Felipe", 12389999], ["Hercolis", 12389999], ["Test", 12389999]]


for i in nomes_telefones:
    print(i[0], i[1])

del nomes_telefones[1]

print('***** Nova lista *******')

for i in nomes_telefones:
    print(i[0], i[1])

