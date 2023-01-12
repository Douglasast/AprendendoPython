def metade(n, format = False):
    valor = n / 2
    if format == False:
        return valor
    else:
        return moeda(valor)


def dobro(n, format = False):
    valor = n * 2
    if format == False:
        return valor
    else:
        return moeda(valor)


def aumentar(n, porcent, format = False):
    valor = n + (n * porcent / 100)
    if format == False:
        return valor
    else:
        return moeda(valor)


def diminuir(n, porcent, format = False):
    valor = n - (n * porcent / 100)
    if format == False:
        return valor
    else:
        return moeda(valor)


def moeda(n, form = "R$"):
    return f'{form}{n:.2f}'.replace('.',',')

def analisar(p, aumento, redução):
    print('======' * 5)
    print('       RESUMO DO VALOR   ')
    print('======' * 5)
    dobro = p * 2
    metade = p / 2
    mais = p + (p * aumento / 100)
    menos = p - (p * redução / 100)
    print('')
    print(f'Preço analisado:    R${p:>.2f}')
    print(f'Dobro do preço:     R${dobro:>.2f}')
    print(f'Metade do preço:    R${metade:>.2f}')
    print(f'{aumento}% de aumento:     R${mais:>.2f}')
    print(f'{redução}% de redução:     R${menos:>.2f}')
    print('')