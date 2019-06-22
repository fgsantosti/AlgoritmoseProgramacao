'''
Faça um programa que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se
que este sofreu um desconto de 10%
'''

preco_produto = float(input('Digite o valor do produto'))

desconto = ((preco_produto*10)/100)

preco_com_desconto = preco_produto - desconto

print('O valor com desconto: ')
print(preco_com_desconto)

print('Seu desconto foi de: ')
print(desconto)