import pandas as pd

# Ler o arquivo CSV e criar um DataFrame
df = pd.read_csv('C:/Users/vinic/Documents/ESTUDOS_DATA_SCIENCE/PORTFÓLIO/IMPORTAÇÃO E EXPORTAÇÃO DO BRASIL DE 1996 A 2023/PAIS.csv', sep=';', encoding='ISO-8859-1', quotechar='"')

# Ver o dataframe
print(df.head())