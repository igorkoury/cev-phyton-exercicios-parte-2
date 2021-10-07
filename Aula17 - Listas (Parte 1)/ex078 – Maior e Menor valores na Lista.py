'''Exercício Python 078: Faça um programa que leia 5 valores numéricos
 e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
 valor digitado e as suas respectivas posições na lista.'''

valores = []
mai = men = 0
for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {v}: ')))
    if v == 0:
        mai = men = valores[0]
    else:
        if valores[v] > mai:
            mai = valores[v]
        if valores[v] < men:
            men = valores[v]
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi {mai}.', end=' ')
for pos, v in enumerate(valores):
    if v == mai:
        print(f'Na posição {pos}.')
print(f'O menor valor digitado foi {men}.', end=' ')
for pos, v in enumerate(valores):
    if v == men:
        print(f'Na posição {pos}.')
