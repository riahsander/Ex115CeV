
#Irá verificar se o arquivo existe
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

#Irá criar o arquivo caso não exista
def criarArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'O arquivo {nome} foi criado com sucesso.')

#Irá ler o arquivo
def lerArq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Não foi possível ler o arquivo!')
    else:
        #cabeçalho pessoas criadas
        print(a.read())
    finally:
        a.close()

#Irá adicionar pessoas 
def cadastrar(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq, 'at') #append text
    except:
        print('Erro ao realizar o cadastrar!')
    else:
        try:
            a.write(f'{nome}, {idade}\n')
        except:
            print('Erro ao adicionar os dados!')
        finally:
            print('Pessoa cadastrada com sucesso.')
            a.close()
