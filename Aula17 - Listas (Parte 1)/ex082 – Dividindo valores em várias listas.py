'''Exercício Python 082: Crie um programa que vai ler vários números
e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

lista = []
par = []
impar = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar adicionando valores a lista? ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Os valores adicionados foram: {lista}')
print(f'O valores PARES adicionados foram {par}')
print(f'Os valores IMPARES adicionados foram: {impar}')
