maioridade = 0
homem = 0
mulher20 = 0
while True:
    sexo = str(input('Qual o sexo? [M/F]: ')).lower()
    while sexo not in 'mf':
        sexo = str(input('Erro, digite novamente. Qual o sexo? [M/F]: ')).lower()
    idade = int(input('Qual a idade?: '))
    while 0 > idade or idade > 110:
        idade = int(input('Idade inválida, tente novamente. Qual a idade?: '))
    print('')
    if idade > 18:
        maioridade += 1
    if sexo == 'm':
        homem += 1
    else:
        if idade < 20:
            mulher20 += 1
    confirm = str(input('Quer continuar?: ')).lower()
    if confirm in 'não':
        break
print(f'{maioridade} pessoas tem mais de 18 anos')
print(f'{homem} pessoas são homens')
print(f'{mulher20} mulheres tem menos de vinte anos')

