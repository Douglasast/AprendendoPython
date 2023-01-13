velho = 0
vnome = ""
menor_de_idade = 0
idade = 0

for p in range(1,5):
    print('')
    nome = str(input(f'Qual o nome da {p}° pessoa?: '))
    genero = str(input('É do sexo masculino ou feminino?: ')).lower()
    i = int(input('Qual a idade?: '))
    idade = idade + i
    if genero in 'm masculino homem':
        if i > velho:
            velho = i
            vnome = nome
    else:
        if i < 20:
            menor_de_idade = menor_de_idade +1

media = idade / 4
print(f'A media de idade do grupo é {media}')
print(f'O homem mais velho do grupo é {vnome}, com {velho} anos de idade')
print(f'O grupo possui {menor_de_idade} mulher/es com menos de 20 anos')
print('')
