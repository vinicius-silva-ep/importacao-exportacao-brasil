import psycopg2
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD


base_path = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_path, "db")


def read_sql_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


verify_schema = os.path.join(db_path, "verify_schema.sql")
create_schema = os.path.join(db_path, "create_schema.sql")
verify_tables = os.path.join(db_path, "verify_tables.sql")
create_tables = os.path.join(db_path, "create_tables.sql")


def db_operations():
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )

        print("Conexão com o banco realizada com sucesso!")
        cursor = connection.cursor()

        cursor.execute(read_sql_file(verify_schema))
        if not cursor.fetchone():
            cursor.execute(read_sql_file(create_schema))
            connection.commit()
            print("Schema 'imp_exp_br' criado com sucesso.")

        cursor.execute(read_sql_file(verify_tables))
        if not cursor.fetchone()[0]:
            cursor.execute(read_sql_file(create_tables))
            connection.commit()
            print("Tabelas criadas com sucesso.")

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Erro ao se conectar com o banco: {e}")
