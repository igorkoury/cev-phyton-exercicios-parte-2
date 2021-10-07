'''Exercício Python 110: Adicione o módulo moeda.py criado nos
desafios anteriores, uma função chamada resumo(), que mostre
na tela algumas informações geradas pelas funções que já temos
no módulo criado até aqui.'''


def aumentar(preço=0, taxa=0, formato=False):
    '''
    -> Calcula o aumento de um determinado preço,
    retornando o resultado formatado ou não.
    :param preço: O preço que se quer reajustar
    :param taxa: A porcentagem do aumento
    :param formato: Se quer a saída foratada ou não
    :return: A saída reajustada, formatada ou não
    '''
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0 ,moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxaA=10, taxaR=10):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print('-' * 30)
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'Aumento de {taxaA}%: \t{aumentar(preço, taxaA, True)}')
    print(f'Redução de {taxaR}%: \t{diminuir(preço, taxaR, True)}')
    print('-' * 30)

# \t -> tabulação
