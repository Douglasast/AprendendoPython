def leiaInt(msg):
    print('-------' * 6)
    numero = str(input(msg))
    while numero.isnumeric() == False:
        print('ERRO! Digite um número inteiro válido.')
        numero = str(input(msg))
    return int(numero)


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o numero: {n}')