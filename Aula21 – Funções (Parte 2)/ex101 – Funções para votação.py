'''Exercício Python 101: Crie um programa que tenha uma função
chamada voto() que vai receber como parâmetro o ano de nascimento
de uma pessoa, retornando um valor literal indicando se uma pessoa
tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''


def voto(ano):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - anoNasc
    if idade < 16:
        return f'Com {idade} anos: NÃO PODE VOTAR'
    elif 18 <= idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'


print('-' * 30)
anoNasc = int(input(f'Em que ano você nasceu? '))
print(voto(anoNasc))
