-- upgrade --
CREATE TABLE IF NOT EXISTS "empresa" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "cnpj_basico" TEXT,
    "razao_social" TEXT,
    "cod_natureza_juridica" TEXT,
    "cod_qualificacao_do_responsavel" TEXT,
    "capital_social" TEXT,
    "cod_porte_da_empresa" TEXT,
    "desc_ente_federativo_responsavel" TEXT,
    "created_at" DATE NOT NULL
);
CREATE TABLE IF NOT EXISTS "estabelecimento" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "cnpj_basico" TEXT,
    "cnpj_ordem" TEXT,
    "cnpj_dv" TEXT,
    "cod_identificador_matriz_filial" TEXT,
    "nome_fantasia" TEXT,
    "cod_situacao_cadastral" TEXT,
    "data_situacao_cadastral" TEXT,
    "cod_motivo_situacao_cadastral" TEXT,
    "end_nome_cidade_no_exterior" TEXT,
    "end_cod_pais" TEXT,
    "data_inicio_atividade" TEXT,
    "cod_cnae_fiscal_primaria" TEXT,
    "cod_cnae_fiscal_secundaria" TEXT,
    "end_tipo_de_logradouro" TEXT,
    "end_logradouro" TEXT,
    "end_numero" TEXT,
    "end_complemento" TEXT,
    "end_bairro" TEXT,
    "end_cep" TEXT,
    "end_uf" TEXT,
    "end_cod_municipio" TEXT,
    "ddd1" TEXT,
    "telefone1" TEXT,
    "ddd2" TEXT,
    "telefone2" TEXT,
    "dddfax" TEXT,
    "fax" TEXT,
    "email" TEXT,
    "cod_situacao_especial" TEXT,
    "data_situacao_especial" TEXT,
    "created_at" DATE NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
