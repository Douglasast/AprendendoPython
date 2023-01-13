print('======' * 5)
print('          BANCO CEV          ')
print('======' * 5)
saque = float(input('Qual valor você quer sacar?: R$'))
cem = saque % 100
nota_cem = int(saque / 100)
cinquenta = cem % 50
nota_cinquenta = int(cem / 50)
vinte = cinquenta % 20
nota_vinte = int(cinquenta / 20)
dez = vinte % 10
nota_dez = int(vinte / 10)
cinco = dez % 5
nota_cinco = int(dez / 5)
dois = cinco % 2
nota_dois = int(cinco / 2)
um = dois % 1
nota_um = int(dois / 1)
print(f'Com o saque de R${saque} você receberá:')
if nota_cem > 0:
    print(f'{nota_cem} notas de R$100. ', end='')
if nota_cinquenta > 0:
    print(f'{nota_cinquenta} notas de R$50. ', end='')
if nota_vinte > 0:
    print(f'{nota_vinte} notas de R$20. ', end='')
if nota_dez > 0:
    print(f'{nota_dez} notas de R$10. ', end='')
if nota_cinco > 0:
    print(f'{nota_cinco} notas de R$5. ', end='')
if nota_dois > 0:
    print(f'{nota_dois} notas de R$2. ', end='')
if nota_um > 0:
    print(f'{nota_um} moedas de R$1. ')
print('')