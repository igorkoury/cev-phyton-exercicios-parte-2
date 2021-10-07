'''
Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo
como criar módulos em Python e reutilizar nossos códigos em outros projetos.
Vamos aprender também como agrupar vários módulos em um pacote, ampliando
ainda mais a modularização em grandes projetos em Python.
'''

# EXEMPLO 01

from uteis import numeros    # também poderia fazer -> 'from uteis import fatorial'

'''
Para chamar a função que está armazenada em outro arquivo.py
basta colocar o nome do arquivo seguido de um ponto -> 'uteis.' 
'''

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} vale {numeros.dobro(num)}')
print(f'O triplo de {num} vale {numeros.triplo(num)}')
