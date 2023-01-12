dados = []
lista = []

print('_Matriz_')

linha = int(input('Quantas linhas a matriz deve ter: '))
coluna = int(input('Quantas colunas a matriz deve ter: '))

for i in range(0, linha):
    for j in range(0, coluna):
        dados.append(int(input(f'Digite um valor para [{i + 1}, {j + 1}]: ')))
    lista.append(dados[:])
    dados.clear()

for i in range(0,linha):
    for j in range(0, coluna):
        print(f'[{lista[i][j]:^5}]', end='')
    print('') 


