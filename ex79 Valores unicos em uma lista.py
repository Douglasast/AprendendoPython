lista = []
for c in range(0,5):
    valor = int(input('Digite um valor: '))
    while valor in lista:
        valor = int(input('Número duplicado, digite outro valor: '))
    lista.append(valor)
print(sorted(lista))