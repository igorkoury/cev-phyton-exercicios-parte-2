'''Nessa aula, vamos continuar nossos estudos de funções em Python,
aprendendo mais sobre Interactive Help em Python, o uso de docstrings
para documentar nossas funções, argumentos opcionais para dar mais
dinamismo em funções Python, escopo de variáveis e retorno de resultados.'''



# DOCSTRINGS

def contador(i, f, p):
    '''
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    '''
    cont = i
    while cont <= f:
        print(f'{cont} ', end='')
        cont += p
    print('FIM')


contador(2, 10, 2)
# 2 4 6 8 10 FIM
help(contador)
# contador(i, f, p)
#     :param i: início da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno




# PARÂMETROS OPCIONAIS

def somar(a=0, b=0, c=0):
    '''
    :param a: primeiro valor a ser somado
    :param b: segundo valor a ser somado
    :param c: terceiro valor a ser somado
    :return: a soma dos valores
    obs: se a quantidade de valores for inferior a quantidade de parâmetros
    o parâmetro que está faltando recebe 0.
    '''
    s = a + b + c
    print(f'A soma dos valores é: {s}')


somar(3, 4, 5)
# A soma dos valores a é: 12
somar(2, 1)
# A soma dos valores a é: 3
somar()
# A soma dos valores a é: 0



# ESCOPO DE VARIÁVEIS - Variável local e global

def teste():
    # Variável local: x - só existe dentro da função teste
    x = 8
    global n
    print(f'Na função teste, N vale {n}')

# Variável global: n - existe dentro e fora da função
n = 2

print(f'No programa principal, N vale {n}')
teste()



# RETORNO DE VALORES

# Retornando valores INT

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram: {r1}, {r2} e {r3}')
# Os resultados foram: 10, 4 e 6

# Retornando valores BOOLEANS

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número inteiro: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
