'''Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
As listas são variáveis compostas que permitem armazenar vários valores em uma
mesma estrutura, acessíveis por chaves individuais.'''

# estrutura da lista - Lista = [ ]

num = [2, 5, 9, 1]
num[2] = 3  # [2, 5, 3, 1] - o número que está na segunda posição recebe 3
num.append(7)  # [2, 5, 3, 1, 7] - adiciona para o final da lista o número 7
num.sort()  # [1, 2, 3, 5, 7] - coloca os elementos em ordem crescente
num.sort(reverse=True)  # [7, 5, 3, 2, 1] - coloca os elementos em ordem decrescente
num.insert(2, 0)  # [7, 5, 0, 3, 2, 1] - na posição 2 adiciona o elemento 0
num.pop()  # [7, 5, 0, 3, 2] - elimina o ultimo elemento da minha lista
num.pop(2)  # [7, 5, 3, 2] - elimina o elemento que está na segunda posição da minha lista
num.remove(2)  # [7, 5, 3] - procura a primeira ocorrencia de um elemento da lista e o elimina, no caso o 2
# num.remove(4)  # ERRO! não há número 4 na lista
if 4 in num:
    num.remove(4)
else:
    print('Não achei o núemro 4')
print(f'Essa lista tem {len(num)} elementos')  # mostra quantos elementos existem na lista
print(num)

a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')  # Lista A: [2, 3, 8, 7]
print(f'Lista B: {b}')  # Lista B: [2, 3, 8, 7]
b = a[:]  # cria uma cópia da lista A em B.
b[2] = 8
print(f'Lista A: {a}')  # Lista A: [2, 3, 4, 7]
print(f'Lista B: {b}')  # Lista B: [2, 3, 8, 7]


# valores = [] or list()

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)  # [5, 9, 4]
for v in valores:
    print(f'{v} ', end='')  # 5 9 4

print('\n')

for pos, v in enumerate(valores):
    print(f'Na posição {pos} encontrei o valor {v}')
# Na posição 0 encontrei o valor 5
# Na posição 1 encontrei o valor 9
# Na posição 2 encontrei o valor 4

lista = list()
for l in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
print(lista, end=' ')  # [1, 2, 3, 4, 5]
print('\n')
for pos, l in enumerate(lista):
    print(f'Na posição {pos} eu encontrei o valor {l}')


