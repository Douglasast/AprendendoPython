import pandas as pd
from Ruxlib import cadastrar

cliente_df = pd.DataFrame(columns= ["Nome", "Idade","CPF","Email"] )
dados = {}

confirmação = ''
while True:

    dados['Nome'] = cadastrar.nome()
    dados['Idade'] = cadastrar.idade()
    dados['CPF'] = cadastrar.CPF()
    dados['Email'] = cadastrar.email()

    cliente_df = cliente_df.append(dados, ignore_index=True)
    dados.clear

    print('Cliente cadastrado')
    confirmação = str(input('Deseja cadastrar mais um Cliente? (s/n): ')).lower()
    if confirmação in 'sim':
        continue
    else:
        break
print(cliente_df)
