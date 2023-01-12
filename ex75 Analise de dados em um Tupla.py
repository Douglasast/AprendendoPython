dados = (int(input('Digite um valor:')),
     int(input('Digite um valor:')), 
     int(input('Digite um valor:')), 
     int(input('Digite um valor:')))
print(f'O valor 9 apareceu {dados.count(9)} vezes')
if 3 in dados:
    print(f'O valor 3 apareceu na {dados.index(3) + 1}° posição.')
else:
    print('O valor 3 não está na lista.')
print('Os números pares são:', end='')
for c in dados:
    if c % 2 == 0:
        print(f' {c}', end='')
print('')
