'''Exercício Python 096: Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno de {l} x {c} = {a}m²')


# Progrma principal
print('-'*30)
print('Controle de Terrenos:')
print('-'*30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
