lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um numero: ')))
    confirm = str(input('Quer continuar? [S/N]: '))
    if confirm in 'Nn':
        break
for c in range(0,len(lista)):
    if lista[c] % 2 == 0:
        pares.append(lista[c])
    else:
        impares.append(lista[c])
print(f'A lista é :{lista}')
print(f'Os numeros pares são: {pares}')
print(f'Os numeros impares são: {impares}')
