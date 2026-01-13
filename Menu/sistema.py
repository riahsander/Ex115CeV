from Library.arquivo import *
from Library.interface import *
from time import sleep

arq = 'cadastro.txt'

if not arquivoExiste(arq):
    criarArq(arq)

while True:
    resposta = menu(['Ver pessoas cadastras',
                     'Cadastrar pessoas',
                     'Sair do programa' ])
    if resposta == 1:
        lerArq(arq)
    elif resposta == 2:
        print(cabecalho('NOVO CADASTRO'))
        nome = str(input('Nome: ').strip().capitalize())
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print(cabecalho('SAINDO DO SISTEMA...ATÉ LOGO!'))
        break 
    else:
        print('ERRO: Não é uma opção válida.')
    sleep(2)