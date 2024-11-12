import requests
import os
import zipfile


def file_download(url, dest_folder):
    response = requests.get(url, verify=False)

    # Obter o nome do arquivo a partir da URL
    filename = os.path.basename(url)
    dest_path = os.path.join(dest_folder, filename)

    # Cria a pasta
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder) 

    # Salva o arquivo
    with open(dest_path, "wb") as new_file:
        new_file.write(response.content)
        print(f"File saved as {dest_path}")

    # Verifica se o arquivo é um arquivo ZIP e extrai para uma pasta com o mesmo nome
    if filename.endswith(".zip"):
        extract_to = os.path.join(
            dest_folder, filename[:-4]
        )  # Remove a extensão ".zip"

        if not os.path.exists(extract_to):
            os.makedirs(extract_to)

        extract_zip(dest_path, extract_to)

        # Remover o aruqivo ZIP após ser extraído
        os.remove(dest_path)


def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"Files extracted to {extract_to}")

# Extrai a lista que está em outro arquivo
from donwload_list import download_list_url

for item in download_list_url:
    file_download(item["url"], item["dest_folder"])