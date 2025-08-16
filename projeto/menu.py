def linha ():
    """
    Exibe uma linha horizontal para separar seções do menu.
    """

    print('-' * 40)


def tabela(frase=''):
    """
    Exibe uma tabela com uma frase centralizada.

    Args:
        frase (str): A frase a ser exibida na tabela.
    """

    linha()
    centrado = frase.center(40)
    print(f'\033[34m{centrado}\033[m')
    linha()


def menu(frase):
    """
    Exibe o menu de opções para o usuário.

    Args:
        frase (str): A frase a ser exibida no topo do menu.

    Returns:
        int: A opção escolhida pelo usuário.
    """

    tabela(frase)
    print('\033[36m1\033[m - Calcular cateto oposto')
    print('\033[36m2\033[m - Calcular cateto adjacente')
    print('\033[36m3\033[m - Calcular hipotenusa')
    print('\033[36m4\033[m - Sair')
    linha()
    opcao = 0
    while opcao < 1 or opcao > 4:
        try:
            opcao = int(input('Escolha uma opção: '))
        except ValueError:
            print('Opção inválida! Tente novamente.')
            linha()
    return opcao