from random import randint
from time import sleep
print('')
print('MEGA SENA')
jogos = int(input('Quantos numeros você quer que eu sorteie?: '))
print(f'Sorteando {jogos} Jogos!')
lista = []
for j in range(0,jogos):
    for n in range(0,6):
        num = randint(1,60)
        while num in lista:
            num = randint(1,60)
        lista.append(num)
    print(f'Jogo {j+1}: {sorted(lista)}')
    sleep(0.5)
    lista.clear()
