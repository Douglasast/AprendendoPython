from random import randint
numeros = []
def sortear():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0,5):
        numeros.append(randint(1, 9))
        print(f'{numeros[c]} ', end='')
    print('/ PRONTO!')

def somar():
    pares = []
    for c in numeros:
        if c % 2 == 0:
            pares.append(c)
    print(f'Somando os valores pares de {numeros}, que são: {pares}, temos {sum(pares)}')


sortear()
somar()
    
