'''Exercício Python 100: Faça um programa que tenha uma lista chamada
 números e duas funções chamadas sorteia() e somaPar(). A primeira
 função vai sortear 5 números e vai colocá-los dentro da lista e a
 segunda função vai mostrar a soma entre todos os valores pares sorteados
 pela função anterior.'''

numeros = list()

from random import randint

def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(0, 10)
        numeros.append(n)
        print(f'{n} ', end='')



sorteia()

def somaPar():
    soma = 0
    for v in numeros:
        if v % 2 == 0:
            soma += v
    print(f'\nA soma dos valores pares em {numeros} é: {soma}')


somaPar()
