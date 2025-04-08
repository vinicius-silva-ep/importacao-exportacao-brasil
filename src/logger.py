import logging
import psycopg2
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT

# Configurações do banco de dados
DB_CONFIG = {
    "dbname": DB_NAME,
    "user": DB_USER,
    "password": DB_PASSWORD,
    "host": DB_HOST,
    "port": DB_PORT,
}


# Classe personalizada para enviar logs ao banco de dados PostgreSQL
class DBHandler(logging.Handler):
    def __init__(self, db_config):
        super().__init__()
        self.conn = psycopg2.connect(
            host=db_config["host"],
            database=db_config["dbname"],
            user=db_config["user"],
            password=db_config["password"],
            port=db_config["port"],
        )
        self.cursor = self.conn.cursor()

        # Criar table se não existir
        self.create_table()

    def create_table(self):
        """Creates the new table if not exists"""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS imp_exp_br.logs (
            id SERIAL PRIMARY KEY,
            creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            table_name VARCHAR(100),
            step VARCHAR(100),
            log_type VARCHAR(50),
            message TEXT        
        );
        """
        try:
            self.cursor.execute(create_table_query)
            self.conn.commit()
        except Exception as e:
            print(f"Error while creating logs table: {e}")

    def emit(self, record):
        try:
            # Rejeitar registros de nível DEBUG
            if record.levelname == "DEBUG":
                return

            # Extrair a message do log e o nível de log
            log_message = self.format(record)
            log_type = record.levelname

            # Obter valores personalizados do registro ou usar padrões
            table = getattr(
                record, "table_name", "imp_exp_br"
            )  # Padrão: "default_table"
            step = getattr(record, "step", "default_step")  # Padrão: "default_step"

            # Inserir log no banco de dados
            query = """
                INSERT INTO imp_exp_br.logs (log_type, message, table_name, step)
                VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(query, (log_type, log_message, table, step))
            self.conn.commit()

        except Exception as e:
            print(f"Error while inserting into table: {e}")

    def close(self):
        """Closing the connection"""
        self.cursor.close()
        self.conn.close()
        super().close()


def setup_logger():
    logger = logging.getLogger()

    # Evitar adicionar handlers duplicados
    if logger.hasHandlers():
        return logger

    # Criar o handler de logs para o banco de dados
    db_handler = DBHandler(DB_CONFIG)
    db_handler.setLevel(logging.INFO)

    # Configurar o logging para usar o handler de banco de dados
    logger.setLevel(logging.DEBUG)
    logger.addHandler(db_handler)

    # Adicionar um handler de console para exibir logs no terminal
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
