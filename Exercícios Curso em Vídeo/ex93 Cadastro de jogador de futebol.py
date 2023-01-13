dados = {}
dados['nome'] = str(input('Nome do Jogador: ')).strip().capitalize() 
primeiro_nome = dados['nome'].split()
p = int(input(f'Quantas partidas {primeiro_nome[0]} jogou: '))
gols = []
for c in range(0,p):
    gols.append(int(input(f'Quantos gols na partida {c+1}: ')))
    total = sum(gols)
dados['gols'] = gols
dados['total'] = total

print('*=*' * 20)
print(dados)
print('*=*' * 20)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')

print('')
print('*=*')
for i, v in enumerate(dados['gols']):
    print(f'Na partida {i + 1}, fez {v} gols.')


