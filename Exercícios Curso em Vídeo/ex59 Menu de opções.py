from time import sleep
print('Menu')
print('')
primeiro_num = int(input('Digite o primeiro número: '))
segundo_num = int(input('Digite o segundo número: '))
opção = 0
while opção < 5:
    print('''
[1] Somar
[2] Multiplicar
[3] Maior e menor
[4] Novos números
[5] Sair do programa
''')
    opção = int(input('Qual opção você quer?: '))
    if opção == 1:
        print(f'A soma é {primeiro_num + segundo_num}')
    elif opção == 2:
        print(f'O produto é {primeiro_num * segundo_num}')
    elif opção == 3:
        if primeiro_num > segundo_num:
            print(f'{primeiro_num} é maior do que {segundo_num}')
        else:
            print(f'{segundo_num} é maior do que {primeiro_num}')
    elif opção == 4:
        primeiro_num = int(input('Digite o primeiro número: '))
        segundo_num = int(input('Digite o segundo número: '))
    elif opção == 5:
        opção = 5
print('Encerrando...')
sleep(1)
print('fim')
