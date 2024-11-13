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
    data_criacao TIMESTAMP default CURRENT_TIMESTAMP
);