'''Exercício Python 107: Crie um módulo chamado moeda.py que tenha
 as funções incorporadas aumentar(), diminuir(), dobro() e metade().
 Faça também um programa que importe esse módulo e use algumas dessas funções.'''

import moeda

p = float(input('Digite o preço do produto: '))
print(f'A metade de {p} vale {moeda.metade(p)}')
print(f'O dobro de {p} vale {moeda.dobro(p)}')
print(f'Aumentando 10% de {p}, temos {moeda.aumentar(p, 10)}')
print(f'Descontando 20% de {p}, temos {moeda.diminuir(p, 20)}')
