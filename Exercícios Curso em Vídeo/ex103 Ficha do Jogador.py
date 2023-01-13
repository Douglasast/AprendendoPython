def ficha():
    print('-------' * 5)
    jogador = str(input('Nome do jogador: '))
    gol = str(input('Número de gols: '))
    if jogador.isalpha():
        jogador = jogador
    else:
        jogador = '<Desconhecido>'
    if gol.isnumeric():
        gol = int(gol)
    else:
        gols = 0
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


ficha()



