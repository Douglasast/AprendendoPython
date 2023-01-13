from random import randint
j = 1
while j > 0:
    escolhido = randint(0,10)
    print('')
    print('Sou seu computador...')
    print('Acabei de pensar em um numero de 0 a 10.')
    print('Será que você consegue advinhar qual foi?')
    print('')
    t = 1
    palpite = int(input('Qual o seu palpite?:'))
    while palpite != escolhido:
        if palpite < escolhido:
            palpite = int(input('Mais... Qual o seu palpite?: '))
        else:
            palpite = int(input('Menos... Qual seu palpite?: '))
        t = t + 1    
    print(f'ACERTOU!!! Na {t}° tentativa!')
    print('')
    jogar = str(input('Quer jogar de novo? [Sim/Não]')).lower().strip()
    if jogar in 'Simssimyesqueroclaroobviopositivoyeah':
        j = 1
    else: 
        j = 0
