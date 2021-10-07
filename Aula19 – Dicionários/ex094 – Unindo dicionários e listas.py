'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input(('Sexo [M/F]: '))).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        cont = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        if cont in 'SN':
            break
        print('ERRO! Digite apenas S ou N')
    if cont == 'N':
        break
# Até aqui somente leitura dos dados, abaixo estão as análises:
print(galera)
print(f'A) Ao todo foram cadaastradas {len(galera)} pessoas')
media = soma / len(galera)
print(f'B) A média das idades foi de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print(f'D) As pessoas que estão acima da média de idade: ', end=' ')
for p in galera:
    if p['idade'] >= media:
        print(f'{p["nome"]}', end=' ')
print()
