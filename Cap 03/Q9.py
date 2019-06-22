'''
Escreva um programa que leia a quantidade de dias, horas, minutos
e segundos do usuário. Calcule o total em segundos.
'''
qnt_dias = int(input())
qnt_horas = int(input())
qnt_minutos = int(input())
qnt_segundos = int(input())
#Um dia tem 24 horas, cada hora tem 60 minutos, cada minuto tem 60 segundos
#Então, um dia em segundos é igual = 24(horas dia) * 60(minutos) * 60(segundos)
qnt_dias_segundos = qnt_dias * (24 * 60 * 60)
qnt_horas_segundos = qnt_horas * 60 * 60
qnt_minutos_segundos = qnt_minutos * 60
print(qnt_dias_segundos)
print(qnt_horas_segundos)
print(qnt_minutos_segundos)
print(qnt_segundos)
total_em_segundos = qnt_dias_segundos + qnt_horas_segundos + qnt_minutos_segundos + qnt_segundos
print(total_em_segundos)

