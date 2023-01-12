from random import choice
from time import sleep
empate = 0
jogador = 0
computador = 0
rodadas = int(input('Quantas vezes você quer jogar?: '))
for c in range(0,rodadas):
     lista = ['PEDRA', 'PAPEL', 'TESOURA']
     escolhido = choice(lista)
     print('''Suas opções:
     [1] PEDRA
     [2] PAPEL
     [3] TESOURA''')
     jogada = str(input('qual é a sua jogada?: ')).lower()
     sleep(0.5)
     print('JO...')
     sleep(0.5)
     print('KEN...')
     sleep(0.5)
     print('PO!')
     if jogada in '1 pedra' and escolhido == 'PEDRA':
          print('''
     O JOGADOR ESCOLHEU (PEDRA)
     O COMPUTADOR ESCOLHEU (PEDRA)

     EMPATE!''')
          empate = empate + 1
     elif jogada in '1 pedra' and escolhido == 'PAPEL':
          print('''
     O JOGADOR ESCOLHEU (PEDRA)
     O COMPUTADOR ESCOLHEU (PAPEL)

     COMPUTADOR VENCEU!''')
          computador = computador + 1
     elif jogada in '1 pedra' and escolhido == 'TESOURA':
          print('''
     O JOGADOR ESCOLHEU (PEDRA)
     O COMPUTADOR ESCOLHEU (TESOURA)

     JOGADOR VENCEU!''')
          jogador = jogador + 1
     elif jogada in '2 papel' and escolhido == 'PEDRA':
          print('''
     O JOGADOR ESCOLHEU (PAPEL)
     O COMPUTADOR ESCOLHEU (PEDRA)
     JOGADOR VENCEU!''')
          jogador = jogador + 1
     elif jogada in '2 papel' and escolhido == 'PAPEL':
          print('''
     O JOGADOR ESCOLHEU (PAPEL)
     O COMPUTADOR ESCOLHEU (PAPEL)
     
     EMPATE!''')
          empate = empate + 1 
     elif jogada in '2 papel' and escolhido == 'TESOURA':
          print('''
     O JOGADOR ESCOLHEU (PAPEL)
     O COMPUTADOR ESCOLHEU (TESOURA)

     COMPUTADOR VENCEU!''')
          computador = computador + 1
     elif jogada in '3 tesoura' and escolhido == 'PEDRA':
          print('''
     O JOGADOR ESCOLHEU (TESOURA)
     O COMPUTADOR ESCOLHEU (PEDRA)

     COMPUTADOR VENCEU!''')
          computador = computador + 1
     elif jogada in '3 tesoura' and escolhido == 'PAPEL':
          print('''
     O JOGADOR ESCOLHEU (TESOURA)
     O COMPUTADOR ESCOLHEU (PAPEL)
     
     JOGADOR VENCEU!''')
          jogador = jogador + 1
     elif jogada in '3 tesoura' and escolhido == 'TESOURA':
          print('''
     O JOGADOR ESCOLHEU (TESOURA)
     O COMPUTADOR ESCOLHEU (TESOURA)

     EMPATE!''')
          empate = empate + 1
print('')
print(f'EMPATE: {empate}')
print(f'VENCEU: {jogador}')
print(f'PERDEU: {computador}')


     
     
     


