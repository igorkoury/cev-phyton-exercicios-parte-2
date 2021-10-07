'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

Exercício Python 093: Crie um programa que gerencie o aproveitamento
de um jogador de futebol. O programa vai ler o nome do jogador e quantas
partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada
partida. No final, tudo isso será guardado em um dicionário, incluindo o
total de gols feitos durante o campeonato.'''

time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for p in range(1, tot+1):
        partidas.append(int(input(f'     Quantos gols {jogador["nome"]} fez nos {p} jogo? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    time.append(jogador.copy())
    while True:
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if resp == 'N':
        break
print('-' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = str(input('Mostrar dados de qual jogador? [999 ENCERRAR]'))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO! Código de jogador inválido.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
