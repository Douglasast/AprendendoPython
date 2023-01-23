from Modulos import modulo_ex107


preço = float(input('Digite o preço: '))
print(f'A metade do preço é: {modulo_ex107.metade(preço)}')
print(f'O dobro do preço é: {modulo_ex107.dobro(preço)}')
print(f'Aumentando 10% é: {modulo_ex107.aumentar(preço, 10)}')
print(f'Reduzindo 15% é: {modulo_ex107.reduzir(preço, 15)}')