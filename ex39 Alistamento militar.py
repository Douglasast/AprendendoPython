from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano em que você nasceu:'))
idade = atual - nascimento
if idade == 18:
    print('faça seu alistamento militar')
elif idade < 18:
    print(f'Você não deve se alistar ainda, faltam {18 - idade} anos')
    print(f'Seu alistamento será em {atual + 18 - idade}')
else:
    print(f'Seu prazo de alistamento já expirou a {idade - 18} anos, vá a uma junta militar o quanto antes para se alistar. ')
    print(f'Seu alistamento deveria ter sido em {atual - (idade - 18)}')


