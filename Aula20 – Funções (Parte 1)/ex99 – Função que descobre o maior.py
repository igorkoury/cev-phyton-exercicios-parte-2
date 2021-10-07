'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros. Seu programa tem que analisar
todos os valores e dizer qual deles é o maior.'''


def maior(* num):
    cont = maior = 0
    print('-' * 40)
    print('\nAnalisando os valores passados:')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0 or valor > maior:
            maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo'
          f' e o maior valor informado foi {maior}')

# Programa principal
maior(2, 6, 8, 10, 11)
maior(3, 5, 7, 1)
