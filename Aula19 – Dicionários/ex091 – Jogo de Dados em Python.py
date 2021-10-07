'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado
 e tenham resultados aleatórios. Guarde esses resultados em um dicionário
 em Python. No final, coloque esse dicionário em ordem, sabendo que o
 vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 01': randint(1, 6),
        'jogador 02': randint(1, 6),
        'jogador 03': randint(1, 6),
        'jogador 04': randint(1, 6)}
ranking = []
print('VALORES SORTEADOR')
for k, v in jogo.items():
    print(f'O {k} tirou: {v}')
    sleep(.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(.5)
