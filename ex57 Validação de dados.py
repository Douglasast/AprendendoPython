sexo = str(input('Qual o sexo? [M/F]: ')).lower().strip()
while sexo not in 'mf':
    sexo = str(input('invalido. informe o sexo [M/F]: ')).lower().strip()
print('fim')