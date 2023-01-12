while True: 
    matriz = []
    valor = []

    print('')
    print('(MATRIZ)')
    linha = int(input('Quantas linhas a matriz tem: '))
    coluna = int(input('Quantas colunas a matriz tem: '))

    for i in range(0, linha):
        for j in range(0, coluna):
            valor.append(int(input(f'valor para [{i + 1},{j + 1}]: ')))
        matriz.append(valor[:])
        valor.clear()

    #mostrando a matriz
    print(f'Matriz {linha}x{coluna}:')
    for i in range(0, linha):
        for j in range(0, coluna):
            print(f'[{matriz[i][j]:^5}]', end='')
        print('')
   
    #somando números pares
    pares = 0
    for i in range(0, linha):
        for j in range(0,coluna):
            if matriz[i][j] % 2 == 0:
                pares += matriz[i][j]
    print(f'A soma de todos os números pares é: {pares}')

    #soma da última coluna
    ultima_coluna = 0
    for i in range(0, linha):
        ultima_coluna += matriz[i][coluna -1]
    print(f'A soma da ultima coluna é: {ultima_coluna}')

    #maior numero da segunda linha, se tiver segunda linha...
    if linha >= 2:
        maior = matriz[1][0]
        for j in range(0, coluna):
                if matriz[1][j] > maior:
                    maior = matriz[1][j]
        print(f'O maior numero da segunda linha é: {maior}')
    else:
        print('A Matriz não possui duas linhas. ')

    print('')
    confirm = str(input('Quer ver outra matriz? [S/N]')).lower()
    if confirm == 'n':
        print('FIM! ')
        break

        


