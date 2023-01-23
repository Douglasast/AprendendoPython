def fatorial(num, show=False):
    '''
    Calcula o Fatorial de um número e mostra na tela.
    :param num: numero.
    :param show: (opcional) False/True, mostra a conta do fatorial
    :return: O valor do fatorial de um numero n.

    '''
    fatorial = 1
    for count in range(num, 0, -1):
        if show == True:
            if count != 1:
                print(f'{count} x ', end='')
            else:
                print(f'{count} = ', end= '')
        fatorial = fatorial * count
    return fatorial


print(fatorial(5))