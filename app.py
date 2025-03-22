from src.extrator.main import extrator
from src.load.db_check import db_operations
from src.load.main import (
    load_and_insert_data,
)  # As operações de extração de dados acontecem aqui

from src.config import *


def main():

    # # Chamar extrator
    try:
        print("Iniciando extração de dados.")
        extrator()
        print("Extração de dados concluída com sucesso.")
    except Exception as e:
        print(f"Erro no extrator: {e}")
        return

    # # Chamar operações no banco de dados
    try:
        print("Iniciando operações de verificações no banco de dados.")
        db_operations()
        print("Verificações no banco de dados concluídas com sucesso.")
    except Exception as e:
        print(f"Erro nas verificações: {e}")
        return

    # # Chamar transformação e carregamento de dados
    try:
        print("Iniciando transformação e carregamento de dados.")
        load_and_insert_data()
        print("Transformação e carregamento de dados concluídos com sucesso.")
    except Exception as e:
        print(f"Erro no processo: {e}")
        return


if __name__ == "__main__":
    main()
