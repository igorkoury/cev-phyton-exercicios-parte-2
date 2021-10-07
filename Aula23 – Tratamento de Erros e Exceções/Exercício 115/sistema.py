'''Exercício 115'''


import lib.interface import *
# from lib.interface import *
from time import sleep
# from lib.arquivo import *


arq = "cursoemvideo.txt"
# Se o arquivo "cursoemvideo.txt" não existir, cria o arquivo.
if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de lista o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        print('Saindo do Sistema...')
        sleep(1)
        cabeçalho('SISTEMA ENCERRADO!')
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida.\033[m')
    sleep(2)
