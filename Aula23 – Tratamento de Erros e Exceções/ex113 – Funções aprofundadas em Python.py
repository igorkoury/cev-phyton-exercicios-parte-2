'''Exercício Python 113: Reescreva a função leiaInt() que fizemos
no desafio 104, incluindo agora a possibilidade da digitação de um
número de tipo inválido. Aproveite e crie também uma função leiaFloat()
com a mesma funcionalidade.'''


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número INTEIRO válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mUsuário prefiriu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número REAL válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mUsuário prefiriu não digitar esse número.\033[m')
            return 0
        else:
            return n


# Programa principal:
inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}.')
