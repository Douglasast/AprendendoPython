import pandas as pd

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'C:/Users/Backup/Documents/GitHub/AprendendoPython/Mini Projetos/Automação de planilha de vendas Excel HashtagProgramação/{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        print(f'No mês de {mes} o vendedor {vendedor} atingiu a meta de R$55.000, conseguindo: R${vendas}')

