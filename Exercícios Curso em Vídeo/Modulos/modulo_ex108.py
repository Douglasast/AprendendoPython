def metade(n):
    valor = n / 2
    return valor

def dobro(n):
    valor = n * 2
    return valor

def aumentar(n, porcent):
    valor = n + (n * porcent / 100)
    return valor

def diminuir(n, porcent):
    valor = n - (n * porcent / 100)
    return valor

def moeda(n = 0, moeda = "R$"):
    return f'{moeda}{n:.2f}'.replace('.',',')

"""OUTRA FORMA


def metade(n):
    valor = n / 2
    return f"R${valor:.2f}".replace('.',',')


def dobro(n):
    valor = n * 2
    return f"R${valor:.2f}"('.',',')


def aumentar(n, porcent=0):
    valor = n + (n * porcent / 100)
    return f"R${valor:.2f}"('.',',')


def reduzir(n, porcent=0):
    valor = n - (n * porcent / 100)
    return f"R${valor:.2f}"('.',',')

"""
