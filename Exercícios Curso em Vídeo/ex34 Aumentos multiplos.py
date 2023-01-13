salario = float(input('Qual o seu salário?: '))
if salario <= 1250:
    print(f'você receberá um aumento de 15%, seu salario sera de R${salario + (salario * 15 /100):.2f}')
else:
    print(f'você receberá um aumento de 10%, seu salario sera de R${salario + (salario * 10 /100):.2f}')
