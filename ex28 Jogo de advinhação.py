from random import choice
n = [1, 2, 3, 4, 5]
escolhido = choice(n)
resposta = int(input('Eu tenho um numero em mente, de 1 a 5, qual você acha que é?: '))
if resposta == escolhido:
    print(f'Parabéns! eu pensei no numero {escolhido}!')
else:
    print(f'Não foi dessa vez, eu pensei no numero {escolhido}!')

#ou
from random import randint
resposta = randint(1 , 5)
escolhido = int(input('Eu tenho um numero em mente, de 1 a 5, qual você acha que é?:'))
if resposta == escolhido:
    print(f'acertou mizeravi, era o {escolhido} mesmo!')
else:
    print(f'errou besta, pensei no {resposta} e não no {escolhido}')





