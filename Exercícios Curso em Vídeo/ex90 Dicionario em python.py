aluno = {}
aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input('Media: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'aprovado'
else:
    aluno['situação'] = 'reprovado'
print(f'O aluno {aluno["nome"]} tem média {aluno["media"]} e sua situação é: {aluno["situação"]}')