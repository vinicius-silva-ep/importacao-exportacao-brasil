import pandas as pd
import os
import sys
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from logger import setup_logger

# Inicializa o logger
logger = setup_logger()


def load_excel_sheet(file_path, sheet_name):
    # Carrega uma planilha específica em um DataFrame.
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        df.columns = (
            df.columns.str.lower()
        )  # Renomeia todas as colunas para minúsculas por conta do Postgres e o sqlalchemy
        df = df.astype(
            str
        )  # Converte todas as colunas para string, para que eu não precise ficar selecionando uma a uma
        df["data_criacao"] = datetime.now()
        logger.info(
            f"DataFrame for sheet '{sheet_name}' created successfully.",
            extra={"table": "imp_exp_br", "step": "transform"},
        )    
        return df
    except ValueError:
        logger.error(
            f"Sheet '{sheet_name}' doesn't exist in the file.",
            extra={"table": "imp_exp_br", "step": "transform"},
        )               
        return None


def transform_data():
    # Carrega planilhas específicas de um arquivo Excel e as armazena em DataFrames.
    # Define o caminho do arquivo
    file_path = os.path.join("data", "TABELAS_AUXILIARES.xlsx")

    # Dataframes a serem carregados
    df_cgce = load_excel_sheet(file_path, sheet_name="3")
    df_isic = load_excel_sheet(file_path, sheet_name="4")
    df_isic_grupo = load_excel_sheet(file_path, sheet_name="16")

    logger.info(
        "All DataFrames were created successfully.",
        extra={"table": "imp_exp_br", "step": "transform"},
    )      

    return df_cgce, df_isic, df_isic_grupo