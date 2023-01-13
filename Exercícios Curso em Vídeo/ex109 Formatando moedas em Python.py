from Modulos import modulo_ex109

p = float(input('Digite o preço: R$'))
print(f'A metade de {modulo_ex109.moeda(p)} é: {modulo_ex109.metade(p, True)}')
print(f'O dobro de {modulo_ex109.moeda(p)} é: {modulo_ex109.dobro(p, True)}')
print(f'Aumentando 10% de {modulo_ex109.moeda(p)} é: {modulo_ex109.aumentar(p, 10, True)}')
print(f'Reduzindo 15% de {modulo_ex109.moeda(p)} é: {modulo_ex109.diminuir(p, 15, True)}')
