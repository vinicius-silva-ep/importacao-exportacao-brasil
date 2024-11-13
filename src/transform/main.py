import pandas as pd
import os


def load_excel_sheet(file_path, sheet_name):
    if os.path.exists(file_path):
        try:
            # Carrega a sheet específica em um DataFrame
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            print(f"Planilha '{sheet_name}' carregada com sucesso.")
            return df
        except ValueError:
            print(f"A planilha '{sheet_name}' não existe no arquivo.")
            return None
    else:
        print(f"O arquivo {file_path} não foi encontrado.")
        return None


if __name__ == "__main__":
    # Define o caminho do arquivo
    file_path = os.path.join("data", "TABELAS_AUXILIARES.xlsx")

    # Dataframe aux_CGCE
    if os.path.exists(file_path):
        try:
            df_isic_grupo = pd.read_excel(file_path, sheet_name="3")
            print("Planilha '3' carregada com sucesso.")
            print(df_isic_grupo)
        except ValueError:
            print("A planilha '3' não existe no arquivo.")
    else:
        print(f"O arquivo {file_path} não foi encontrado.")

    # Dataframe aux_ISIC
    if os.path.exists(file_path):
        try:
            df_isic = pd.read_excel(file_path, sheet_name="4")
            print("Planilha '4' carregada com sucesso.")
            print(df_isic)
        except ValueError:
            print("A planilha '4' não existe no arquivo.")
    else:
        print(f"O arquivo {file_path} não foi encontrado.")

    # Dataframe aux_ISIC_GRUPO
    if os.path.exists(file_path):
        try:
            df_isic_grupo = pd.read_excel(file_path, sheet_name="16")
            print("Planilha '16' carregada com sucesso.")
            print(df_isic_grupo)
        except ValueError:
            print("A planilha '16' não existe no arquivo.")
    else:
        print(f"O arquivo {file_path} não foi encontrado.")
