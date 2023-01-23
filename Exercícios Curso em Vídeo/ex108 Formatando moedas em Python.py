from Modulos import modulo_ex108


preço = float(input('Digite o preço: R$'))
print(f'A metade de {modulo_ex108.moeda(preço)} é: {modulo_ex108.moeda(modulo_ex108.metade(preço))}')
print(f'O dobro de {modulo_ex108.moeda(preço)} é: {modulo_ex108.moeda(modulo_ex108.dobro(preço))}')
print(f'Aumentando 10% de {modulo_ex108.moeda(preço)} é: {modulo_ex108.moeda(modulo_ex108.aumentar(preço, 10))}')
print(f'Reduzindo 15% de {modulo_ex108.moeda(preço)} é: {modulo_ex108.moeda(modulo_ex108.diminuir(preço, 15))}')

