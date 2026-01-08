from Library.arquivo import *

arq = 'cadastro.txt'

if not arquivoExiste(arq):
    criarArq(arq)