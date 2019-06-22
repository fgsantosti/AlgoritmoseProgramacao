'''
Faça um programa que receba uma hora (uma variável para hora e outra para minutos), calcule e
mostre:
a) a hora digitada convertida em minutos;
b) o total dos minutos, ou seja, os minutos digitados mais a conversão anterior;
c) o total dos minutos convertidos em segundos
'''

hora = int(input('Digite a hora: '))

minutos = int(input('Digite a minutos: '))

horas_em_minutos = hora * 60

hora_convertida_minutos = horas_em_minutos + minutos

print('hora digitada convertida em minutos: ', hora_convertida_minutos)