lista = [[], []]
valor = 0
for c in range(0,7):
    valor = int(input('Digite um numero:'))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(f'Os numeros pares são: {sorted(lista[0])}')
print(f'Os numeros impares são: {sorted(lista[1])}')