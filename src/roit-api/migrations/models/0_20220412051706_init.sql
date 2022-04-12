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
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
