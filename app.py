from src.extrator.main import extrator
from src.load.db_check import db_operations
from src.load.main import (
    load_and_insert_data,
)  # As operações de extração de dados acontecem aqui
from src.transform.main import transform_data

from src.config import *

import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from logger import setup_logger

# Inicializa o logger
logger = setup_logger()


def main():

    # # Chamar extrator
    try:
        logger.info(
            f"-- 1. Starting the data extraction process --",
            extra={"table": "imp_exp_br", "step": "general ETL"},
        )         
        extrator()
        logger.info(
            f"-- 1. Finishing the data extraction process --",
            extra={"table": "imp_exp_br", "step": "general ETL"},
        )         
    except Exception as e:
        logger.error(
            f"-- 1. Error during extraction: {e} --",
            extra={"table": "imp_exp_br", "step": "general ETL"},
        )          
        return
    
    # # Chamar operações no banco de dados
    try:
        logger.info(
            f"-- 2. Starting the database operations process --",
            extra={"table": "imp_exp_br", "step": "general ETL"},
        )            
        db_operations()
        logger.info(
            f"-- 2. Finishing the database operations process --",
            extra={"table": "imp_exp_br", "step": "general ETL"},
        )         
    except Exception as e:
        logger.error(
            f"-- 2. Error during database operations: {e} --",
            extra={"table": "imp_exp_br", "step": "general ETL"},
        ) 
        return

    # # Chamar transformação e carregamento de dados
    try:
        logger.info(
            f"-- 3. Starting data transformation and loading --",
            extra={"table": "imp_exp_br", "step": "general ETL"},
        )        
        load_and_insert_data()
        logger.info(
            f"-- 3. Finishing data transformation and loading --",
            extra={"table": "imp_exp_br", "step": "general ETL"},
        )            
    except Exception as e:
        logger.error(
            f"-- 3. Error during data transformation and loading: {e} --",
            extra={"table": "imp_exp_br", "step": "general ETL"},
        ) 
        return


if __name__ == "__main__":
    main()
