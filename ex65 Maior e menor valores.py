maior = 0
menor = 0
soma = 0
count = 0
confirm = 'sim'
while confirm in "sim":
    valor = int(input('Digite um valor: '))
    count += 1
    soma += valor
    if count == 1:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
    confirm = str(input('Quer continuar?: [Sim/Não]')).lower()
media = soma / count
print(f'O maior é {maior}')
print(f'O menor é {menor}')
print(f'A media entre eles é {media}')