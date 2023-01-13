from random import randint
count = 0
while True:
    escolhido = randint(1,10)
    jogador = int(input('Escolha um número de 1 a 10: '))
    resultado = (escolhido + jogador) % 2
    ou = str(input('Par ou impar? [P/I]: ')).lower()
    if ou == 'p':
        n = 0
    else:
        n = 1
    if resultado == n:
        count = count + 1
        print('Você acertou!')
        print(f'Você escolheu {jogador} e o computador escolheu {escolhido}, resultando em {jogador + escolhido}')
    else: 
        print('Você PERDEU!')
        print(f'Você escolheu {jogador} e o computador escolheu {escolhido}, resultando em {jogador + escolhido}')
        break
print(f'Você venceu {count} vezes seguidas')
    

