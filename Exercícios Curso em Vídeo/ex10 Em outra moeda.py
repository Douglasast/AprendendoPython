real = float(input('quanto dinheiro você tem na carteira?: '))
dolar = real / 5.34
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))