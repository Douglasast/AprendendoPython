gasto = 0
milhar = 0
barato = ''
count = 0
menor = 0

while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: '))
    gasto = gasto + preço

    if preço > 1000:
        milhar = milhar + 1
    
    count = count + 1
    if count == 1:
        barato = produto
        menor = preço
    else:
        if preço < menor :
            barato = produto
            menor = preço

    confirm = str(input('Quer continuar?: [S/N]')).lower()
    while confirm not in 'simnãonao':
        confirm = str(input('Tente novamente. Quer continuar? [S/N]: ')).lower()
    if confirm not in 'sim':
        break

print(f'{milhar} produtos custam mais de mil reais')
print(f'O total da compra foi R${gasto:.2f} ')
print(f'O produto mais barato foi "{barato}" que custou R${menor:.2f}')
