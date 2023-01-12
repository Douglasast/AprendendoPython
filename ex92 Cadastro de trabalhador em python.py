from datetime import datetime
cadastro = {}
cadastro['nome'] = str(input('Nome: ')).strip().capitalize()
ano = int(input('Ano de Nascimento: '))
cadastro['idade'] = datetime.now().year - ano

carteira = int(input('Carteira de Trabalho, [Digite 0 se você não tem.]: '))
if carteira == 0:
    for k, v in cadastro.items():
        print(f'{k} tem o valor {v}')
else:
    cadastro['CTPS'] = carteira
    cadastro['contratação'] = int(input('Ano de Contratação: '))
    cadastro['salario'] = int(input('salário: '))
    cadastro['aposentadoria'] = (cadastro['contratação'] + 35) + cadastro['idade'] - datetime.now().year
    for k, v in cadastro.items():
        print(f'{k} tem o valor {v}')
