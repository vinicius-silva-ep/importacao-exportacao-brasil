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

        # Criar tabela se não existir
        self.create_table()

    def create_table(self):
        """Cria a tabela de logs se ela não existir."""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS imp_exp_br.logs (
            id SERIAL PRIMARY KEY,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            tabela VARCHAR(100),
            etapa VARCHAR(100),
            tipo_log VARCHAR(50),
            mensagem TEXT        
        );
        """
        try:
            self.cursor.execute(create_table_query)
            self.conn.commit()
        except Exception as e:
            print(f"Erro ao criar tabela de logs: {e}")

    def emit(self, record):
        try:
            # Rejeitar registros de nível DEBUG
            if record.levelname == "DEBUG":
                return

            # Extrair a mensagem do log e o nível de log
            log_mensagem = self.format(record)
            tipo_log = record.levelname

            # Obter valores personalizados do registro ou usar padrões
            tabela = getattr(
                record, "tabela", "default_table"
            )  # Padrão: "default_table"
            etapa = getattr(record, "etapa", "default_step")  # Padrão: "default_step"

            # Inserir log no banco de dados
            query = """
                INSERT INTO imp_exp_br.logs (tipo_log, mensagem, tabela, etapa)
                VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(query, (tipo_log, log_mensagem, tabela, etapa))
            self.conn.commit()

        except Exception as e:
            print(f"Erro ao inserir log no banco de dados: {e}")

    def close(self):
        """Fecha a conexão com o banco de dados."""
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
