'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

listaValores = list()
while True:
    val = int(input('Digite um valor: '))
    if val not in listaValores:
        listaValores.append(val)
        print('Valor adicionado a lista com SUCESSO!')
    else:
        print('Valor duplicado. Tente um outro valor.')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar adicionando valores? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
listaValores.sort()
print(f'Os valores adicionados na lista foram: {listaValores}')
