import pandas as pd
import os
from datetime import datetime


def load_excel_sheet(file_path, sheet_name):
    # Carrega uma planilha específica em um DataFrame.
    if os.path.exists(file_path):
        try:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            df.columns = (
                df.columns.str.lower()
            )  # Renomeia todas as colunas para minúsculas por conta do Postgres e o sqlalchemy
            df = df.astype(
                str
            )  # Converte todas as colunas para string, para que eu não precise ficar selecionando uma a uma
            df["data_criacao"] = datetime.now()
            return df
        except ValueError:
            print(f"A planilha '{sheet_name}' não existe no arquivo.")
            return None
    else:
        print(f"O arquivo {file_path} não foi encontrado.")
        return None


def transform_data():
    # Carrega planilhas específicas de um arquivo Excel e as armazena em DataFrames.
    # Define o caminho do arquivo
    file_path = os.path.join("data", "TABELAS_AUXILIARES.xlsx")

    # Dataframes a serem carregados
    df_cgce = load_excel_sheet(file_path, sheet_name="3")
    df_isic = load_excel_sheet(file_path, sheet_name="4")
    df_isic_grupo = load_excel_sheet(file_path, sheet_name="16")

    return df_cgce, df_isic, df_isic_grupo
