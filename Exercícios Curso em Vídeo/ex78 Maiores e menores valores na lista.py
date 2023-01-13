lista = []
maior = 0
menor = 0
for c in range(0,5):
    lista.append(int(input('Digite um valor:')))
    if c == 0:
        maior = lista[0]
        menor = lista[0]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'O maior é numero {maior}, na posição {lista.index(maior) + 1}')
print(f'O menor é numero {menor}, na posição {lista.index(menor) + 1}')

#OU

lista = []
for c in range(0,5):
    lista.append(int(input('Digite um valor:')))
lista.sort()
print(f'O maior é numero {lista[0]}, na posição 1')
print(f'O menor é numero {lista[-1]}, na posição 5')
