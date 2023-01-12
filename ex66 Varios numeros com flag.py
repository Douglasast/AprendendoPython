numero = 0
count = 0
soma = 0
while True:
    numero = int(input('Digite um número [999 encerra]: '))
    if numero == 999:
        break
    soma = soma + numero
    count = count + 1
print(f'{count} foram números digitados e a soma total entre eles é {soma}')
