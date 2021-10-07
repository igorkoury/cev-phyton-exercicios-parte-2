'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = somaCol = maior2Lin = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite número para [{l},{c}]: '))
print('=' * 60)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
    print()
print(f'a) A soma dos valores pares é {somaPar}')
for l in range(0, 3):
    somaCol += matriz[l][2]
print(f'b) A soma dos valores digitados na terceira coluna: {somaCol}')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior2Lin:
        maior2Lin = matriz[1][c]
print(f'c) O maior valor da segunda coluna: {maior2Lin}')
