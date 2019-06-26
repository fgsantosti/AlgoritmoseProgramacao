
import agenda as a

def entrar_sistema():
    login = input('Digite seu login: ')
    senha = input('Digite seu senha: ')

    if(login == "fgs" and senha == "ifpi2019"):
        a.menu()
    else:
        print('Digite sua senha novamente ou deseja sair?')
        print('1 - Digitar senha \n0 - Sair ')
        op = int(input('Digite a opção: '))

        while True:
            if op == 1:
                entrar_sistema()
            elif op == 0:
                break

entrar_sistema()
        
        
