'''Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
As listas são variáveis compostas que permitem armazenar vários valores em uma
mesma estrutura, acessíveis por chaves individuais.'''

dados = ['Igor', 28]
dados.append('Lailane')
dados.append(31)
pessoas = [dados[:]]
print(pessoas)
print(dados)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

print(galera[0])  # ['João', 19]
print(galera[0][0])  # João

for pessoa in galera:
    print(pessoa[0])
# João
# João
# Ana
# Joaquim
# Maria

for pessoa in galera:
    print(pessoa[1])
# 19
# 33
# 13
# 45

for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')
# João tem 19 anos de idade
# Ana tem 33 anos de idade
# Joaquim tem 13 anos de idade
# Maria tem 45 anos de idade

#________________________________________________________

galera = []
dados = []
totMaior = totMenor = 0
for cont in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
print(dados)
# []
print(galera)
# [['Pedro', '22'], ['Ana', '30'], ['Igor', '28']]

for pes in galera:
    if pes[1] >= 21:
        print(f'{pes[0]} é maior de idade e tem {pes[1]} anos')
        totMaior += 1
    else:
        print(f'{pes[0]} é menor de idade e tem {pes[1]} anos')
        totMenor += 1
print(f'Temos {totMaior} maiores e {totMenor} menores de idade')
# Pedro é maior de idade e tem 22 anos
# Ana é maior de idade e tem 33 anos
# Igor é maior de idade e tem 28 anos
# Temos 3 maiores e 0 menores de idade

