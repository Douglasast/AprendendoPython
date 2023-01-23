def ajuda():
    while True:
        print('-----' * 5)
        print('SISTEMA DE AJUDA PyHELP')
        print('-----' * 5)
        print()
        FunçãoBiblioteca = str(input('Função ou Biblioteca: ')).strip().lower()
        if FunçãoBiblioteca == 'fim':
            break
        print('-----' * 5)
        print(f'Acessando o manual do comando {FunçãoBiblioteca}')
        print('-----' * 5)
        print()
        help(FunçãoBiblioteca)
print('Fim do programa')
ajuda()
