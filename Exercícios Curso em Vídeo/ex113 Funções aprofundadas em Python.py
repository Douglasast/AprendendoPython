def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('Erro, Digite um número inteiro valido.')
            continue
        else:
            return num


def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('Erro, Digite um número real valido.')
            continue
        else:
            return num


inteiro = leiaint('Digite um número inteiro:')
real = leiafloat('Digite um número real:')
print(f'O número inteiro digitado foi {inteiro} e o real foi {real}')