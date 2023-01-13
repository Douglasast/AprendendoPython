dados = {}
lista = []
mulheres = []
tot_idade = 0
while True:
    dados['nome'] = str(input('Nome: '))
    idade = int(input('Idade: '))
    tot_idade += idade
    dados['idade'] = idade

    sexo = str(input('Sexo [M/F]: ')).upper()
    while sexo not in 'MF':
        print('Erro! Por favor, digite apenas M ou F.')
        sexo = str(input('Sexo [M/F]: ')).upper()
    dados['sexo'] = sexo
    if sexo == 'F':
        mulheres.append(dados['nome'])


    lista.append(dados.copy())
    confirm = str(input('Quer continuar? [S/N]')).upper()
    while confirm not in 'SN':
        print('Erro! Por favor, digite apenas S ou N.')
        confirm = str(input('Quer continuar? [S/N]')).upper()
    if confirm == 'N':
        break

media = tot_idade / len(lista)

print(f'Foram registradas {len(lista)} pessoas')
print(f'A média das idades é {tot_idade / len(lista)}')

# mulheres cadastradas
if len(mulheres) > 0:
    print('As mulheres cadastradas foram: ', end='')
    for i, v in enumerate(mulheres):
        print(v)

#pessoas acima da idade media
print('As pessoas acima da idade média são: ')
for p in lista:
    if p['idade'] > media:
        for k, v in p.items():
            print(f'{k} = {v}')
