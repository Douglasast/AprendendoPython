n = int(input('Digite um numero: '))
opção = str(input('''Para qual base numerica você quer converter?
(1)Binário.
(2)Hexadecimal.
(3)Octal.
: ''')).lower()
if opção in 'binario binário primeiro primeira 1':
    print(f'{n} convertido para Binário é {bin(n)}')
elif opção in 'hexadecimal hexa hex hexadesimal 2 segunda segundo':
    print(f'{n} convertido para Hexadecimal é {hex(n)}')
elif opção in 'Octal octa oct terceira terceiro 3':
    print(f'{n} convertido para Octal é {oct(n)}')
else:
    print('Não entendi, tente novamente')
