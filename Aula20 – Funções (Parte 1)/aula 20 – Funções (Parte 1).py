'''Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar
funções em Python. Funções são trechos de código que podem ser executados
em momentos diferentes de nossos códigos em Python. Veja como funciona o
comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.'''

def mostralinha():
    print('-'*30)


mostralinha()
print(f'{"   IGOR   "}')
mostralinha()


def titulo(msg):
    mostralinha()
    print(f'{   msg   }')
    mostralinha()

titulo('            IGOR')

# Rotina que pode se tornar uma função
a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)

# Programa principal
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


soma(4, 5)
soma(8, 9)
soma(2, 1)

# Empacotamento de parâmetros
def contador(* num):
    print(num)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
# (2, 1, 7)
# (8, 0)
# (4, 4, 7, 6, 2)

# Empacotamento de parâmetros
def contador(* num):
    tamanho = len(num)
    print(f'Recebi os valores {num} e são ao todo {tamanho} números')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
# Recebi os valores (2, 1, 7) e são no total 3 números
# Recebi os valores (8, 0) e são no total 2 números
# Recebi os valores (4, 4, 7, 6, 2) e são no total 5 números

# Dobrando valores em uma lista usando uma função
def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
# [14, 4, 10, 0, 8]

# Somando valores em uma lista usando uma função
def soma(* valores):
    s = 0
    for num in valores:
        s = s + num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
# Somando os valores (5, 2) temos 7
# Somando os valores (2, 9, 4) temos 15