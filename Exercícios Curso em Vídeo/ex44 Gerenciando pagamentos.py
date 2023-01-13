valor = float(input('Digite o valor a ser pago: R$'))
print('''Os meios de pagamento são:
(1) À vista em dinheiro ou cheque com 10% de desconto.
(2) À vista no cartão com 5% de desconto.
(3) Até duas vezes no cartão, preço formal.
(4) 3x ou mais no cartão''')
pagamento = int(input('Digite o número do meio de pagamento que você deseja: '))
if pagamento == 1:
    print(f'O valor será de R${valor - (valor * 10 /100):.2f}')
elif pagamento == 2:
    print(f'O valor será de R${valor - (valor * 5 /100):.2f}')
elif pagamento == 3:
    print(f'O valor será o mesmo e cada parcela será de R${valor/2:.2f} por mês')
elif pagamento == 4:
    parcelas = int(input('Em quantas parcelas?: '))
    preço = valor + (valor * 20 /100)
    print(f'O valor será de R${preço:.2f} e cada parcela será de R${preço / parcelas:.2f}')
else:
    print('Meio de pagamento inválido, tente novamente.')



