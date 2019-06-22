
salario_atual = float(input('Digite o seu salário atual: '))

if(salario_atual > 500):
    salario_novo = salario_atual + (salario_atual * 10 / 100)
else:
    salario_novo = salario_atual + (salario_atual * 20 / 100)

print('O seu novo salário é: ', salario_novo)
