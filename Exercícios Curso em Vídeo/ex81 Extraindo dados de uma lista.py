lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    confirm = str(input('Quer continuar? [S/N]'))
    if confirm in 'Nn':
        break
print(f'{len(lista)} valores foram digitados.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')