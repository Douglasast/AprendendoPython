print('Consulta de emprestimo.')
casa = float(input('Qual o valor da casa?: '))
salario = float(input('Qual o valor do seu salário?: '))
anos = int(input('Em quantos anos você deseja pagar?: '))
prestação = casa / (anos * 12)
if prestação > (salario * 30) / 100:
    print(f'Seu emprestimo foi negado pois o valor da prestação mensal: R${prestação:.2f} ultrapassa os 30% do seu salario')
else:
    print(f'Seu emprestimo foi aprovado')