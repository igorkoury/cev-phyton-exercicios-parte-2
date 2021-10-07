'''Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar
dicionários em Python. Os dicionários são variáveis compostas que permitem
armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.'''

# dicionário - dic = {} ou dic = dict()

# EXEMPLO 01

dados = {'Nome': 'Pedro', 'Idade': 25}
print(dados['Nome'])
# Pedro
print(dados['Idade'])
# 25

# Adicionando um elemento ao dicionário:
dados['Sexo'] = 'M'
print(dados['Sexo'])
# M
dados = {'Nome': 'Pedro', 'Idade': 25, 'Sexo': 'M'}

# Remover um elemento:
del dados['Idade']
dados = {'Nome': 'Pedro', 'Sexo': 'M'}

# EXEMPLO 02

filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'}

# Imprimindo os valores:
print(filme.values())
# dict_values(['Star Wars', 1977, 'George Lucas'])

# Imprimindo as chaves:
print(filme.keys())
# dict_keys(['titulo', 'ano', 'diretor'])

# Imprimindo o dicionário inteiro:
print(filme.items())
# dict_items([('titulo', 'Star Wars'), ('ano', 1977), ('diretor', 'George Lucas')])

# Usando laço para imprimir o dicionário completo:
for k, v in filme.items():
    print(f'O {k} é {v}')
# O titulo é Star Wars
# O ano é 1977
# O diretor é George Lucas
