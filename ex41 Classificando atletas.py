from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
if idade <= 9:
    print(f'Com {idade} anos o atleta é da categoria MIRIM')
elif idade > 9 and idade <= 14:
    print(f'Com {idade} anos o atleta é da categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print(f'Com {idade} anos o atleta é da categoria JÚNIOR')
elif idade > 19 and idade <=25:
    print(f'Com {idade} anos o atleta é da categoria SÊNIOR')
elif idade > 25:
    print(f'Com {idade} anos o atleta é da categoria MASTER')

#ou os elif podem ser <= 14 <=19 <=25 >25