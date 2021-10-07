'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

dados = []
pessoas = []
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso [kg] : ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Os dados cadastrados foram {pessoas}')
print(f'Você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {mai}kg: ', end=' ')
for p in pessoas:
    if p[1] == mai:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso foi de {men}kg: ', end=' ')
for p in pessoas:
    if p[1] == men:
        print(f'{p[0]}')
