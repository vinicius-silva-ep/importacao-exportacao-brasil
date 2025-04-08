import os
import sys
from sqlalchemy import create_engine

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logger import setup_logger

# Inicializa o logger
logger = setup_logger()

from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD, DB_SCHEMA
from transform.main import transform_data


pwd = DB_PASSWORD
postgres_user = DB_USER
postgres_host = DB_HOST
postgres_port = DB_PORT
postgres_database = DB_NAME
postgres_schema = DB_SCHEMA


connection_string = f"cockroachdb+psycopg2://{postgres_user}:{pwd}@{postgres_host}:{postgres_port}/{postgres_database}"





def load_and_insert_data():

    engine = create_engine(connection_string)

    try:

        df_cgce, df_isic, df_isic_grupo = transform_data()
        
        # Insere dados na tabela 'cgce'
        rows_cgce = df_cgce.shape[0]
        df_cgce.to_sql(
            "cgce", engine, schema=postgres_schema, if_exists="replace", index=False
        )
        logger.info(
            f"{rows_cgce} records inserted into the 'cgce' table",
            extra={"table": "imp_exp_br", "step": "load"},
        )            

        # Insere dados na tabela 'isic'
        rows_isic = df_isic.shape[0]
        df_isic.to_sql(
            "isic", engine, schema=postgres_schema, if_exists="replace", index=False
        )
        logger.info(
            f"{rows_isic} records inserted into the 'isic' table",
            extra={"table": "imp_exp_br", "step": "load"},
        )                    

        # Insere dados na tabela 'isic_grupo'
        rows_isic_grupo = df_isic_grupo.shape[0]
        df_isic_grupo.to_sql(
            "isic_grupo",
            engine,
            schema=postgres_schema,
            if_exists="replace",
            index=False,
        )
        logger.info(
            f"{rows_isic_grupo} records inserted into the 'isic_grupo' table",
            extra={"table": "imp_exp_br", "step": "load"},
        )        

    except Exception as e:
        logger.error(
            f"Error inserting data: {e}",
            extra={"table": "imp_exp_br", "step": "transform"},
        )        
