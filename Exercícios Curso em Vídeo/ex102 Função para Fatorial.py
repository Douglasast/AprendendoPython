def fatorial(n, show=False):
    '''
    Calcula o Fatorial de um numero e mostra na tela.
    :param n: numero.
    :param show: (opcional) False/True, mostra a conta do fatorial
    :return: O valor do fatorial de um numero n.

    '''
    f = 1
    for c in range(n, 0, -1):
        if show == True:
            if c != 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end= '')
        f = f * c
    return f


print(fatorial(5))