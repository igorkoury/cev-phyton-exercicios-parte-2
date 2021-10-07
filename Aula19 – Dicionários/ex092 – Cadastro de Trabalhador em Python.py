'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e
carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso
a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e
o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
from datetime import datetime
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho [0 não possui]: '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = (dados['contratação'] + 35) - nasc
print('=' * 30)
for k, v in dados.items():
    print(f'- {k} tem o valor {v}')
