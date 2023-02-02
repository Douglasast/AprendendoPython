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


#Criando e mostrando dataframe apenas com a colunas importantes e na ordem desejada
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


#Lendo uma tabela de um banco de dados SQL:
import pandas as pd
import mysql.connector


conexão = mysql.connector.connect(
  host="hostname",
  user="nome de usuário",
  password="senha",
  database="nome do banco de dados")
tabela_sql = pd.read_sql_query('SELECT * FROM tabela', conexão)

print(tabela_sql)



