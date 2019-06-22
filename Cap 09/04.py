
produto = []

def inserir_produto():
    arq = open('produtos', 'a')
    print('Inserir produtos \n')
    nome = input('Nome: ')
    preco = float(input('Preço:'))
    arq.write("%s - %f\n" % (nome, preco))
    arq.close()

def listar_produtos():
    arq = open('produtos', 'r')
    print('Lista de todos os produtos \n')
    for i in arq.readlines():
        nome, preco = i.strip().split("-")
        preco = float(preco)
        
        print('Nome =>', nome)
        print('Preço => %.2f'% preco)

    arq.close()

while True:
    print('__________Menu________')
    print('1-Inserir produto')
    print('2-Listar todos os produtos')
    print('0-Sair')
    op = int(input('Digite a opcao:'))
    if(op == 1):
        inserir_produto()
    elif(op == 2):
        listar_produtos()
    else:
        break
