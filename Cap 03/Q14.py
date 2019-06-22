
ano_nasc  = int(input('Ano nascimentos: '))
ano_atual = int(input('Ano atual: '))

idade   = ano_atual - ano_nasc
meses   = idade * 12
dias    = idade * 365
semanas = dias / 7

print('A idade dessa pessoa em anos: ', idade)
print('A idade dessa pessoa em meses: ', meses)
print('A idade dessa pessoa em semanas: ', semanas)
print('A idade dessa pessoa em dias: ', dias)




