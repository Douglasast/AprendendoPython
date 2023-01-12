from Modulos import modulo_ex108


p = float(input('Digite o preço: R$'))
print(f'A metade de {modulo_ex108.moeda(p)} é: {modulo_ex108.moeda(modulo_ex108.metade(p))}')
print(f'O dobro de {modulo_ex108.moeda(p)} é: {modulo_ex108.moeda(modulo_ex108.dobro(p))}')
print(f'Aumentando 10% de {modulo_ex108.moeda(p)} é: {modulo_ex108.moeda(modulo_ex108.aumentar(p, 10))}')
print(f'Reduzindo 15% de {modulo_ex108.moeda(p)} é: {modulo_ex108.moeda(modulo_ex108.diminuir(p, 15))}')

