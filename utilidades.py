def separar_por_linha():
    print('-'*82)


def vermelho(palavra):
    print(f'\u001b[31m{palavra}\u001b[0m')


def verde(palavra):
    print(f'\u001b[32m{palavra}\u001b[0m')


def amarelo(palavra):
    print(f'\u001b[33m{palavra}\u001b[0m')


def azul(palavra):
    print(f'\u001b[34m{palavra}\u001b[0m')


def apresentar_programa():
    '''
    CORES ANSII
    vermelha \u001b[31m
    verde \u001b[32m
    amarela \u001b[33m
    azul \u001b[34m

    \u001b[0m'
    '''
    separar_por_linha()
    print(' ' * 30 + '\u001b[32mINVISTA-ME\u001b[0m')
    print(' '*25 + 'Pronto para investir?')
    separar_por_linha()
