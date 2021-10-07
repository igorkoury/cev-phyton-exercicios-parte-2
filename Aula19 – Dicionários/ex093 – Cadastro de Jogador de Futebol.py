'''Exercício Python 093: Crie um programa que gerencie o aproveitamento
de um jogador de futebol. O programa vai ler o nome do jogador e quantas
partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada
partida. No final, tudo isso será guardado em um dicionário, incluindo o
total de gols feitos durante o campeonato.'''

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for p in range(1, tot+1):
    partidas.append(int(input(f'     Quantos gols {jogador["nome"]} fez nos {p} jogo? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('='*30)

# Resultado no formato de dicionário
print(jogador)
# {'nome': 'Igor', 'gols': [4, 5, 6], 'total': 15}

print('='*30)

# Resultado genérico
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
# O campo nome tem o valor Igor
# O campo gols tem o valor [4, 5, 6]
# O campo total tem o valor 15

print('='*30)

# Resultado mais detalhado e completo
print(f'O jogador {jogador["nome"]} jogou {tot} partidas.')
for i, v in enumerate(partidas):
    print(f'   => Na partida {i+1}, fez {v} gols.')
print(f'O total de gols foi {jogador["total"]}')
# O jogador Igor jogou 3 partidas.
#    => Na partida 1, fez 4 gols.
#    => Na partida 2, fez 5 gols.
#    => Na partida 3, fez 6 gols.
# O total de gols foi 15
