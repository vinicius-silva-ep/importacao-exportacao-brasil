import pandas as pd

caminho_arquivo = 'C:/Users/vinic/Documents/ESTUDOS_DATA_SCIENCE/PORTFÓLIO/IMPORTAÇÃO E EXPORTAÇÃO DO BRASIL DE 1996 A 2023/EXP_COMPLETA/EXP_COMPLETA.csv'

dados = pd.read_csv(caminho_arquivo)

for coluna in dados.columns:
    maior_tamanho = dados[coluna].astype(str).apply(len).max()
    print(f"A maior tamanho em caracteres na coluna {coluna} é: {maior_tamanho}")