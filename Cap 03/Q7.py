'''
Faça um programa que receba o peso de uma pessoa, calcule e mostre:
a) o novo peso, se a pessoa engordar 15% sobre o peso digitado;
b) o novo peso, se a pessoa emagrecer 20% sobre o peso digitado.
'''
peso_pessoa = float(input('Digite seu peso: '))

peso_ganho = (peso_pessoa * 15) / 100

peso_perda = (peso_pessoa * 20) / 100

peso_final_ganho = peso_pessoa + peso_ganho

peso_final_perda = peso_pessoa - peso_perda

print('O seu peso final ganho é: ')

print(peso_final_ganho)

print('O seu peso final perda é: ')

print(peso_final_perda)

