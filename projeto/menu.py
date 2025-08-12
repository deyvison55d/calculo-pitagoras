def linha ():
    print('-' * 40)


def tabela():
    linha()
    print(f'{'Calculo de Pitágoras':^40}')
    linha()


def menu():
    tabela()
    print('1 - Calcular cateto oposto')
    print('2 - Calcular cateto adjacente')
    print('3 - Calcular hipotenusa')
    print('4 - Sair')
    linha()
    opcao = 0
    while opcao < 1 or opcao > 4:
        try:
            opcao = int(input('Escolha uma opção: '))
        except ValueError:
            print('Opção inválida! Tente novamente.')
            linha()
    return opcao