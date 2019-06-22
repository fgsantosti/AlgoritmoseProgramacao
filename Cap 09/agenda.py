
#criando uma lista vazia 
agenda = []

def pede_nome():
    return (input("Nome: "))
def pede_telefone():
    return (input("Telefone: "))

def novo():
    global agenda
    #abre o arquivo com o modo a+
    arquivo = open("agenda.txt", "a+", encoding="utf-8")
    #pega o nome e o telefone    
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])

    #gravando no arquivo agenda.txt
    for e in agenda:
        arquivo.write("%s#%s\n" % (e[0], e[1]))
    arquivo.close()

def ler():
    global agenda
    arquivo = open("agenda.txt", "r", encoding="utf-8")
    agenda = []
    for l in arquivo.readlines():		
        nome, telefone = l.strip().split("#")
        agenda.append([nome, telefone])
    arquivo.close()

    print ("\nContatos da Agenda\n\n------")
    i = 0
    for e in agenda:
        print (i," - Nome: %s Telefone: %s" % (e[0], e[1]))
        i = i + 1

def excluir():
    arquivo = open("agenda.txt", "r", encoding="utf-8")
    agenda = []
    for l in arquivo.readlines():		
        nome, telefone = l.strip().split("#")
        agenda.append([nome, telefone])
    arquivo.close()

    ler()
    idcontato = int(input('Digite o id do contato:'))
    del agenda[idcontato]

    #gravando no arquivo agenda.txt com o modo w
    arquivo = open("agenda.txt", "w", encoding="utf-8")
    for e in agenda:
        arquivo.write("%s#%s\n" % (e[0], e[1]))
    arquivo.close()
    
    
def menu():
    print ("""
        1 - Novo
        2 - Ler
        3 - Excluir
        0 - Sai
    """)
    op = int(input("Escolha uma opção: "))
    return op

while True:
    opcao = menu()
    if opcao == 0:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        ler()
    elif opcao == 3:
        excluir()
