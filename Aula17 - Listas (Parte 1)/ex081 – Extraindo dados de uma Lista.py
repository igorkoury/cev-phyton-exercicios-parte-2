'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
cont = 0
while True:
    lista.append(int(input('Digite um número: ')))
    print('Valor adicionado com sucesso!')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
lista.sort(reverse=True)
print('Os valores adicionados na lista foram: ', end='')
for n in lista:
    print(f'{n}', end=' ')
print(f'\nVocê adicionou {len(lista)} números na lista.')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 NÃO está na lista.')
