lista = []
dados = []
n = 0
while True:
    dados.append(str(input('NOME: ')))
    dados.append(int(input('PESO: ')))
    lista.append(dados[:])
    dados.clear()
    confirm = str(input('Quer continuar? [S/N]: ')).lower()
    n = n + 1
    if confirm == 'n':
        break

print(f'{n} pessoas foram cadastradas.')

pesadas = 0
for p in lista:
    if p[1] >= 100:
        pesadas += 1
        print(f'{p[0]} ', end='')
if pesadas > 0:
    print('são pessoas pesadas')

leves = 0
for p in lista:
    if p[1] <= 70:
        leves += 1
        print(f'{p[0]} ', end='')
if leves > 0:
    print('são pessoas leves')
    
    



lista = []
dados = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    lista.append(dados[:])
    dados.clear()
    confirm = str(input('Quer continuar? [S/N]: ')).lower()
    if confirm == 'n':
        break
pesadas = []
leves = []
for p in lista:
    if p[1] >= 100:
        pesadas.append(p[0])
    elif p[1] <= 70:
        leves.append(p[0])
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'{pesadas} são pessoas pesadas')
print(f'{leves} são pessoas leves')
print('fim')

#maior e menor
lista = []
dados = []
maior = 0
menor = 0
while True:
    dados.append(str(input('NOME: ')))
    dados.append(str(input('PESO: ')))
    lista.append(dados[:])
    confirm = str(input('Quer continuar? [S/N]: ')).lower()
    if confirm == 'n':
        break
    if len(lista) == 0:
        maior = dados[1]
        menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    dados.clear()
    print(f'O maior peso foi {maior}KG')
    print(f'O menor peso foi {menor}KG')
    print(f'Foi registrado {len(lista)} pessoas')