'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários
alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo
a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

boletim = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 01: '))
    nota2 = float(input('Nota 02: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? :')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{"Núm.":<10}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i, a in enumerate(boletim):
    print(f'{i:<10}{a[0]:<10}{a[2]:>8}')
    opc = ' '
while True:
    opc = int(input('Mostrar notas de qual aluno? [999 para interromper] '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(boletim) - 1:
        print(f'Notas de {boletim[opc][0]} são {boletim[opc][1]}')
print('VOLTE SEMPRE')
