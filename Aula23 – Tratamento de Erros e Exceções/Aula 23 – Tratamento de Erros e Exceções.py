'''Nessa aula, vamos ver como o Python permite tratar erros e criar
respostas a essas exceções. Aprenda como usar a estrutura try
except no Python de uma forma simples.'''

# TENTATIVA
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

# FALHOU
except Exception as erro:
    print(f'Infelizmente tivemos um problema... :('
          f'O problema encontrado foi {erro.__class__}')

# DEU CERTO
else: #
    print(f'O resultado é {r:.1f}')

# CERTO / FALHA
finally:
    print('Volte sempre muito obrigado!')



# CADA 'TRY' PODE TER VÁRIOS 'EXCEPT':

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

# UTILIZANDO VÁRIOS 'EXCEPT's EM UM MESMO 'TRY'
except (ValueError, TypeError):
    print('ERRO! Tivemos um problema com os tipos de dados que você digitou... :(')
except ZeroDivisionError:
    print('ERRO! Não é possível dividir um número por "zero"!')
except KeyboardInterrupt:
    print('ERRO! O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encotrado foi {erro.__cause__}')

else:
    print(f'O resultado é {r:.1f}')

finally:
    print('Volte sempre muito obrigado!')
