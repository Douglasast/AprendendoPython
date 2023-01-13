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
