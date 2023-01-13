def ajuda():
    while True:
        print('-----' * 5)
        print('SISTEMA DE AJUDA PyHELP')
        print('-----' * 5)
        print()
        f = str(input('Função ou Biblioteca: ')).strip().lower()
        if f == 'fim':
            break
        print('-----' * 5)
        print(f'Acessando o manual do comando {f}')
        print('-----' * 5)
        print()
        help(f)
print('Fim do programa')
ajuda()
