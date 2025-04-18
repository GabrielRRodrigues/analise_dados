# Passo a passo
# Passo 1: Importar a base de dados
import pandas as pd

tabela = pd.read_csv('clientes.csv', encoding='latin', sep=';')

# deletar a coluna inútil
# axis(eixo) - 0 = linha / 1 = coluna
tabela = tabela.drop('Unnamed: 8', axis=1)

# Passo 2: Visualizar a base de dados
# print(tabela.info())
# Entender as informações disponíveis 
# Procurar erros na base de dados
    # células vazias
    # tipo de dados

# Passo 3: Tratamento de Dados

tabela['Salário Anual (R$)'] = pd.to_numeric(tabela['Salário Anual (R$)'], errors='coerce')  # ignore(ignorar) ou coerce(forçar)

tabela = tabela.dropna()  # limpar células vazias
# print(tabela[tabela['Profissão'].isna()]) # exibir células vazias

# Passo 4: Análise Inicial -> Entender as notas dos clientes
print(tabela.describe())  # Descrição de dados

import plotly.express as px
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, y='Nota (1-100)', histfunc= 'avg', text_auto= True) #nbins = 0 - agrupamentos
    grafico.show()

# Passo 5: Análise Completa - > entender como cada características do ciente impacta na nota
    # Idade: Relevância a partir de 15 anos
    # Profissão: Entretenimento e Artista
    # Experiência: 10 a 15 anos
    # Família: até 7 membros
# print(tabela.info())
