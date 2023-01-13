from datetime import date

atual = date.today().year
quantidade = int(input('verificar quantas pessoas?: '))
maioridade = 0

for c in range(0,quantidade):
    nascimento = int(input('Ano de nascimento:'))
    idade = atual - nascimento
    if idade >= 18:
        maioridade += 1
        
print(f'{maioridade} pessoas são maiores de idade e {quantidade - maioridade} não menores de idade.')