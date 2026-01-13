from Library.arquivo import *

#Irá printar as linhas para organização
def linha(tam = 42):
    return '-' * tam

#Irá criar o cabeçalho do menu
def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

#Irá verificar se a opção escolhida pelo usuário é válida
def leiaInt(msg):
    while True:
        try:
            num_int = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Não foi digitado uma opção válida.')
        else:
            return num_int

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[032m{c}\033[m - \033[034m{item}\033[m')
        c += 1
    print(linha())
    #Irá ler a opção digitada pelo usuário
    opcao = leiaInt('Sua opção: ')
    return opcao