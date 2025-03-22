import os
import requests


def download_file(url, save_directory="data"):
    # Extrai o nome do arquivo da URL
    file_name = url.split("/")[-1]
    save_path = os.path.join(save_directory, file_name)

    # Faz a requisição para baixar o arquivo
    response = requests.get(url)
    if response.status_code == 200:
        # Salva o conteúdo na pasta especificada
        with open(save_path, "wb") as file:
            file.write(response.content)
        print(f"Arquivo '{file_name}' baixado com sucesso e salvo em: {save_path}")
    else:
        print(
            f"Falha no download de '{file_name}'. Status code: {response.status_code}"
        )


def extrator():
    # Lista de URLs para download
    urls = [
        "https://balanca.economia.gov.br/balanca/bd/tabelas/TABELAS_AUXILIARES.xlsx",
    ]

    # Cria a pasta "data" caso ela não exista
    os.makedirs("data", exist_ok=True)

    # Realiza o download de cada arquivo na lista
    for url in urls:
        download_file(url)
