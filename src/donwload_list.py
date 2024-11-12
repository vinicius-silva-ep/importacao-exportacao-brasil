# Site oficial - https://www.gov.br/mdic/pt-br/assuntos/comercio-exterior/estatisticas/base-de-dados-bruta
# Lista de URLs e destinos

download_list_url = [

    # Dados de Países
    {
        "url": "https://balanca.economia.gov.br/balanca/bd/tabelas/PAIS.csv",
        "dest_folder": "C:/Users/vinic/Documents/ESTUDOS_DATA_SCIENCE/PORTFÓLIO/IMPORTAÇÃO E EXPORTAÇÃO DO BRASIL DE 1996 A 2023"
    },

    # # Dados de exportação 
    # {
    #     "url": "https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_COMPLETA.zip",
    #     "dest_folder": "C:/Users/vinic/Documents/ESTUDOS_DATA_SCIENCE/PORTFÓLIO/IMPORTAÇÃO E EXPORTAÇÃO DO BRASIL DE 1996 A 2023"
    # },

    # # Dados de importação
    # {
    #     "url": "https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/IMP_COMPLETA.zip",
    #     "dest_folder": "C:/Users/vinic/Documents/ESTUDOS_DATA_SCIENCE/PORTFÓLIO/IMPORTAÇÃO E EXPORTAÇÃO DO BRASIL DE 1996 A 2023"
    # },
    
    # Dados de Blocos
    {
        "url": "https://balanca.economia.gov.br/balanca/bd/tabelas/PAIS_BLOCO.csv",
        "dest_folder": "C:/Users/vinic/Documents/ESTUDOS_DATA_SCIENCE/PORTFÓLIO/IMPORTAÇÃO E EXPORTAÇÃO DO BRASIL DE 1996 A 2023"
    },

    # NCM
    {
        "url": "https://balanca.economia.gov.br/balanca/bd/tabelas/NCM.csv",
        "dest_folder": "C:/Users/vinic/Documents/ESTUDOS_DATA_SCIENCE/PORTFÓLIO/IMPORTAÇÃO E EXPORTAÇÃO DO BRASIL DE 1996 A 2023"
    },

    # NCM - Unidade
    {
        "url": "https://balanca.economia.gov.br/balanca/bd/tabelas/NCM_UNIDADE.csv",
        "dest_folder": "C:/Users/vinic/Documents/ESTUDOS_DATA_SCIENCE/PORTFÓLIO/IMPORTAÇÃO E EXPORTAÇÃO DO BRASIL DE 1996 A 2023"
    },

    # Via
    {
        "url": "https://balanca.economia.gov.br/balanca/bd/tabelas/VIA.csv",
        "dest_folder": "C:/Users/vinic/Documents/ESTUDOS_DATA_SCIENCE/PORTFÓLIO/IMPORTAÇÃO E EXPORTAÇÃO DO BRASIL DE 1996 A 2023"
    },

    # URF - Unidade da RFB
    {
        "url": "https://balanca.economia.gov.br/balanca/bd/tabelas/URF.csv",
        "dest_folder": "C:/Users/vinic/Documents/ESTUDOS_DATA_SCIENCE/PORTFÓLIO/IMPORTAÇÃO E EXPORTAÇÃO DO BRASIL DE 1996 A 2023"
    },

    # ISIC  - Classificação Internacional de Todas Atividades Econômicas
    {
        "url": "https://balanca.economia.gov.br/balanca/bd/tabelas/NCM_ISIC.csv",
        "dest_folder": "C:/Users/vinic/Documents/ESTUDOS_DATA_SCIENCE/PORTFÓLIO/IMPORTAÇÃO E EXPORTAÇÃO DO BRASIL DE 1996 A 2023"
    }                        

]

# Quando for necessário testar para ver se não há nenhum erro na lista
# print(download_list_url)