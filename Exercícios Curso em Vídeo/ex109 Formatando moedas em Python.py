from Modulos import modulo_ex109

preço = float(input('Digite o preço: R$'))
print(f'A metade de {modulo_ex109.moeda(preço)} é: {modulo_ex109.metade(preço, True)}')
print(f'O dobro de {modulo_ex109.moeda(preço)} é: {modulo_ex109.dobro(preço, True)}')
print(f'Aumentando 10% de {modulo_ex109.moeda(preço)} é: {modulo_ex109.aumentar(preço, 10, True)}')
print(f'Reduzindo 15% de {modulo_ex109.moeda(preço)} é: {modulo_ex109.diminuir(preço, 15, True)}')
