itens = ('Lapis', 1.00,
        'Caderno', 10.50,
        'Borracha', 0.50,
        'Estojo', 8.20,
        'Compasso', 3.25, 
        'Mochila', 78.99,
        'Caneta', 1.20,
        'Livro', 29.99,
        'Transferidor', 2.50)

print('-' * 30)
print(f'{"Lista de Preços":^30}')
print('-' * 30)
print('')
for c in range(0, len(itens)):
    if c % 2 == 0:
        print(f'{itens[c]:.<30}', end='') 
    else:
        print(f' R${itens[c]:.2f}')
print('')
print('-' * 30)