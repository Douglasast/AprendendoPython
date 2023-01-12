def analisar(*valores):
    print()
    print('=====' * 10)
    print('Analisando valores passados...')
    maior = 0
    for c in valores:
        print(f'{c} ', end='')
        if c > maior:
            maior = c
    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
    print('=====' * 10)
    print()

analisar(1, 3, 5, 2, 6, 77, 4)
