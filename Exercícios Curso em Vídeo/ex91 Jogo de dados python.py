from random import randint
from operator import itemgetter

jogos = {'jogador 1': randint(1,6),
         'jogador 2': randint(1,6),
         'jogador 3': randint(1,6),
         'jogador 4': randint(1,6)}

for k, v in jogos.items():
    print(f'O {k} tirou {v} no dado.')

print('*=*' * 10)

ranking = []
ranking = sorted(jogos.items(), key=itemgetter(1), reverse = True)

print('RANKING DOS JOGADORES')
for i, v in enumerate(ranking):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}')
