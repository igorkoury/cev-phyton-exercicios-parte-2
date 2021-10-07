'''Exercício Python 114: Crie um código em Python que
teste se o site pudim está acessível pelo computador usado.'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.erro.URLError:
    print('Não foi possível acessar o site no momento.')
else:
    print('O site Pudim foi acessado com sucesso.')
    print(site.read()) # OPCIONAL: consegue ler o conteúdo html do site acessado

