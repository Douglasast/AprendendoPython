peso = int(input('Qual seu peso(kg)?:' ))
altura = float(input('Qual sua altura(m)?:'))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é {imc:.1f}, ', end='')
if imc < 18.5:
    print('abaixo do peso.')
elif imc <= 25:
    print('peso ideal.')
elif imc <= 30:
    print('sobrepeso.')
elif imc <= 40:
    print('Obesidade.')
elif imc > 40:
    print('Obesidade Mórbida.')