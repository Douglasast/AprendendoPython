print('Somando vários valores:')
contador = 0
soma = 0
numero = int(input('Digite um número:'))
while numero != 999:
    soma += numero
    contador += 1
    numero = int(input('Digite um número [999 para encerrar]:'))
print(f'Foram digitados {contador + 1} numeros! E a soma de todos eles é {soma}')
