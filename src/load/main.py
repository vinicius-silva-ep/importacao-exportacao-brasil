import os
import sys
from sqlalchemy import create_engine

# from sqlalchemy import create_engine

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD, DB_SCHEMA
from transform.main import transform_data
from db_check import db_operations


pwd = DB_PASSWORD
postgres_user = DB_USER
postgres_host = DB_HOST
postgres_port = DB_PORT
postgres_database = DB_NAME
postgres_schema = DB_SCHEMA


connection_string = f"cockroachdb+psycopg2://{postgres_user}:{pwd}@{postgres_host}:{postgres_port}/{postgres_database}"


df_cgce, df_isic, df_isic_grupo = transform_data()


def load_and_insert_data():

    engine = create_engine(connection_string)

    df_cgce.to_sql(
        "cgce", engine, schema=postgres_schema, if_exists="replace", index=False
    )
    print("Dados inseridos")


db_operations()
load_and_insert_data()
