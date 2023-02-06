import pandas as pd

#criando um dataframe vazio:
df = pd.DataFrame()


#Criando um dataframe usando um dicionário:
Pessoa = {'Nome': ['Willow', 'Wilson'], 
        'Idade': [19, 21],
        'Nacionalidade': ['Constant','Constant'],}
Tabela_pessoa = pd.DataFrame(Pessoa)


#Mostrando um dataframe: 
print(Tabela_pessoa)


#Criando e mostrando um dataframe apenas com a colunas importantes e na ordem desejada
Pessoa = {'Nome': ['Willow', 'Wilson'], 
        'Idade': [19, 21],
        'Nacionalidade': ['Constant','Constant'],}
Tabela_pessoa = pd.DataFrame(Pessoa, columns=['Nacionalidade','Nome'])
print(Tabela_pessoa)


#Lendo um arquivo Excel/.xlsx:
planilha_df = pd.read_excel('C:/Users/Backup/Documents/GitHub/AprendendoPython/Mini Projetos/Teste Pandas/Abril.xlsx')


#Mostrando um dado do arquivo, [Coluna][linha]:
print(planilha_df['Vendas'][8])


#mostrando apenas o inicio do DataFrame:
print(planilha_df.head(10))


#mostrando o número de colunas e linhas:
print(planilha_df.shape)


#atribuindo uma coluna / pd.series a uma variavel:
vendas = planilha_df['Vendas']


#descrevendo de modo geral um DataFrame:
print(planilha_df.describe())


#comando .loc
#padrão
teste = planilha_df.loc['linha', 'coluna']
#mostrar linhas especificas:
print(planilha_df.loc[1:5])

#pegando linhas que correspondem a uma condição:
Menor_Rendimento_df = planilha_df.loc[planilha_df['Vendas'] < 45000]

#pegando linhas que correspondem a uma condição e apenas as colunas desejadas
Menor_Rendimento_df = planilha_df.loc[planilha_df['Vendas'] < 45000, ['Somente','Colunas','Escolhidas']]


#Criando novas colunas:
#Criando uma coluna apartir de outra:
planilha_df['Comissão'] = planilha_df['Vendas'] * 0.05

#Criando uma coluna com valor padrão:
planilha_df.loc[:,'Exemplo'] = 0

#Adicionando linhas apartir de outro arquivo:
planilha_df = planilha_df.append('OutroArquivo.xlsx')











