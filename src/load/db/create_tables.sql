-- CGCE

create table if not exists imp_exp_br.cgce (
    CO_NCM text,
    NO_NCM_POR text,
    CO_CGCE_N3 text,
    NO_CGCE_N3 text,
    NO_CGCE_N3_ING text,
    NO_CGCE_N3_ESP text,
    CO_CGCE_N2 text,
    NO_CGCE_N2 text,
    NO_CGCE_N2_ING text,
    NO_CGCE_N2_ESP text,
    CO_CGCE_N1 text,
    NO_CGCE_N1 text,
    NO_CGCE_N1_ING text,
    NO_CGCE_N1_ESP text,
    data_criacao TIMESTAMP
);

-- ISIC

create table if not exists imp_exp_br.isic (
    CO_NCM text,
    NO_NCM_POR text,
    CO_ISIC_CLASSE text,
    NO_ISIC_CLASSE text,
    NO_ISIC_CLASSE_ING text,
    NO_ISIC_CLASSE_ESP text,
    CO_ISIC_GRUPO text,
    NO_ISIC_GRUPO text,
    NO_ISIC_GRUPO_ING text,
    NO_ISIC_GRUPO_ESP text,
    CO_ISIC_DIVISAO text,
    NO_ISIC_DIVISAO text,
    NO_ISIC_DIVISAO_ING text,
    NO_ISIC_DIVISAO_ESP text,
    CO_ISIC_SECAO text,
    NO_ISIC_SECAO text,
    NO_ISIC_SECAO_ING text,
    NO_ISIC_SECAO_ESP text,
    data_criacao TIMESTAMP
);

-- ISIC GRUPO

create table if not exists imp_exp_br.isic_grupo (
    CO_NCM text,
    NO_NCM_POR text,
    CO_ISIC_SECAO text,
    NO_ISIC_SECAO text,
    CO_CUCI_GRUPO text,
    NO_CUCI_GRUPO text,
    data_criacao TIMESTAMP
);