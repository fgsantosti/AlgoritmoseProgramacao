'''
Faça um programa que preencha um vetor com seis elementos numéricos inteiros.
Calcule e mostre:
- todos os números pares; ok
- todos os números ímpares; ok 
- a quantidade de números ímpares; 
- a quantidade de números pares;
'''

vetor_numeros = []
quant_pares = 0
quant_impares = 0
#preecher o vetor
for i in range(6):
    vetor_numeros.append(int(input("Digite um numero: ")))

#mostrando todos os pares
for i in range(6):
    if(vetor_numeros[i]%2==0):
        print(vetor_numeros[i], " é par")
        quant_pares = quant_pares + 1 

#todos os números ímpares;
for i in range(6):
    if(vetor_numeros[i]%2 != 0):
        print(vetor_numeros[i], " é impar")
        quant_impares = quant_impares + 1

print('a quantidade de números ímpares é:', quant_impares)

print('a quantidade de números pares é:', quant_pares)


