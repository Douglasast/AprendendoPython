lista = []
dados = []
while True:
        dados.append(str(input('Nome: ')))
        dados.append(float(input('Nota 1: ')))
        dados.append(float(input('Nota 2: ')))
        lista.append(dados[:])
        dados.clear()
        confirm = str(input('Quer continuar? [S/N]: ')).lower()
        if confirm == 'n':
            break
print('')
for c in range(0,len(lista)):
    print(f'Aluno {c + 1}: {lista[c][0]} , média: {(lista[c][1] + lista[c][2]) / 2}' )
print('')
nota = int(input('Quer ver a nota de qual aluno?: '))
print(f'Aluno {lista[nota - 1][0]} teve as notas: {lista[nota -1][1]} e {lista[nota -1][2]}')