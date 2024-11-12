import os
import chardet

# Esse código serve para codificar todos os arquivos csv em csv com encoding utf-8 - vpereira - 27/02/2024

def verificar_codificacao_utf8(arquivo_path):
    with open(arquivo_path, 'rb') as f:
        resultado = chardet.detect(f.read(10000))
    
    codificacao_detectada = resultado['encoding']

    if codificacao_detectada.lower() == 'utf-8':
        print(f'O arquivo {arquivo_path} já está codificado em UTF-8.')
    else:
        print(f'O arquivo {arquivo_path} não está codificado em UTF-8. A codificação detectada é: {codificacao_detectada}')
        converter_para_utf8(arquivo_path)

def converter_para_utf8(arquivo_path):
    with open(arquivo_path, 'r', encoding='ISO-8859-1') as f:
        conteudo = f.read()

    with open(arquivo_path, 'w', encoding='utf-8') as f:
        f.write(conteudo)

    print(f'O arquivo {arquivo_path} foi convertido para UTF-8.')

def verificar_e_converter_csv_em_lote(diretorio):
    for nome_arquivo in os.listdir(diretorio):
        arquivo_path = os.path.join(diretorio, nome_arquivo)
        if os.path.isfile(arquivo_path) and arquivo_path.lower().endswith('.csv'):
            verificar_codificacao_utf8(arquivo_path)

def main():
    diretorio = 'C://Users//vinic//Documents//ESTUDOS_DATA_SCIENCE//PORTFÓLIO//IMPORTAÇÃO E EXPORTAÇÃO DO BRASIL DE 1996 A 2023'
    verificar_e_converter_csv_em_lote(diretorio)

if __name__ == "__main__":
    main()
