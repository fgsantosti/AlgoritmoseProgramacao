salario = float(input(''))
if(salario>1250):
    valor_aumento = (salario*10)/100
elif(salario > 0 and salario<=1250):
    valor_aumento = (salario*15)/100
elif(salario <= 0):
    print('Não houve produção')

print(valor_aumento)
