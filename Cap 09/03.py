
def escreve_nome():
    arq = open('nome_alunos', 'a')
    nome = input('Insira seu nome: ')
    arq.write("%s\n" % nome)
    arq.close()

def mostrar_nomes():
    arq = open('nome_alunos', 'r')
    j = 0
    for i in arq.readlines():
        j+=1
        print(j,' - Aluno: ', i)
    arq.close()


while True:
    print('__________Menu________')
    print('1-Inserir aluno')
    print('2-Listar todos os alunos')
    print('0-Sair')
    op = int(input('Digite a opcao:'))
    if(op == 1):
        escreve_nome()
    elif(op == 2):
        mostrar_nomes()
    else:
        break

