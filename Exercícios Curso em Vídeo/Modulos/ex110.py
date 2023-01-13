def moeda(p, aumento, redução):
    print('======' * 5)
    print('       RESUMO DO VALOR   ')
    print('======' * 5)
    dobro = p * 2
    metade = p / 2
    mais = p + (p * aumento / 100)
    menos = p - (p * redução / 100)
    print('')
    print(f'Preço analisado:    R${p:>.2f}')
    print(f'Dobro do preço:     R${dobro:>.2f}')
    print(f'Metade do preço:    R${metade:>.2f}')
    print(f'{aumento}% de aumento:     R${mais:>.2f}')
    print(f'{redução}% de redução:     R${menos:>.2f}')
    print('')

