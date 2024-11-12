import csv
import psycopg2

# Conectar ao banco de dados PostgreSQL
connection = psycopg2.connect(
    host="xxxxx",
    port=26257,
    database="dw_estudos",
    user="vinicius",
    password="xxxxx",
    sslmode="require"
)

# Verificar se a conexão foi estabelecida com sucesso
if connection:
    print("Conexão realizada com sucesso")

cursor = connection.cursor()

file_path = 'C:\\Users\\vinic\\Documents\\ESTUDOS_DATA_SCIENCE\\PORTFÓLIO\\IMPORTAÇÃO E EXPORTAÇÃO DO BRASIL DE 1996 A 2023\\teste_municipios.csv'

# Especificar o codec ao abrir o arquivo
with open(file_path, 'r', encoding='utf-8') as f:
    next(f)  # Pula a linha de cabeçalho
    cursor.copy_expert(f"COPY municipios FROM STDIN WITH CSV DELIMITER ';'", file=f)

connection.commit()
