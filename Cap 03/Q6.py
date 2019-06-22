'''
Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um programa
que receba o salário fixo do funcionário e o valor de suas vendas, calcule e mostre a comissão e seu
salário final.
'''

salario_fixo = float(input('Digite o salário fixo: '))

valor_vendas = float(input('Digite o valor de vendas: '))

valor_comissao = (valor_vendas * 4)/ 100

salario_final = salario_fixo + valor_comissao

print('Valor final do salário: ')
print(salario_final)
print('Valor de comissão: ')
print(valor_comissao)
