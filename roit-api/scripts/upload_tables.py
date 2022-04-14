import os
from urllib.parse import urlparse

import pandas as pd
import psycopg2


QUERY_EMPRESA = """INSERT INTO empresa(
            cnpj_basico,
            razao_social,
            cod_natureza_juridica,
            cod_qualificacao_do_responsavel,
            capital_social,
            cod_porte_da_empresa,
            desc_ente_federativo_responsavel,
            created_at)
            values (%s, %s, %s, %s, %s, %s, %s, %s)
        """

QUERY_ESTABELECIMENTO = """INSERT INTO estabelecimento(
            cnpj_basico,
            cnpj_ordem,
            cnpj_dv,
            cod_identificador_matriz_filial,
            nome_fantasia,
            cod_situacao_cadastral,
            data_situacao_cadastral,
            cod_motivo_situacao_cadastral,
            end_nome_cidade_no_exterior,
            end_cod_pais,
            data_inicio_atividade,
            cod_cnae_fiscal_primaria,
            cod_cnae_fiscal_secundaria,
            end_tipo_de_logradouro,
            end_logradouro,
            end_numero,
            end_complemento,
            end_bairro,
            end_cep,
            end_uf,
            end_cod_municipio,
            ddd1,
            telefone1,
            ddd2,
            telefone2,
            dddfax,
            fax,
            email,
            cod_situacao_especial,
            data_situacao_especial,
            created_at)
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """


def connect():
    # result = urlparse(os.environ.get("DATABASE_URL"))
    result = urlparse("postgres://postgres:postgres@web-db:5432/web_dev")
    username = result.username
    password = result.password
    database = result.path[1:]
    hostname = str(input("Qual o IPAddress?"))
    port = result.port
    return psycopg2.connect(
        database = database,
        user = username,
        password = password,
        host = hostname,
        port = port
    )


def load_file(name):
    return pd.read_csv(f'./data/{name}.csv').astype(str)


def insert_table(conn, table, query):
    values = []
    cursor = conn.cursor()
    print("Iniciando inserção de dados...")
    df = load_file(table)
    
    for row in df.itertuples():
        try:
            values.append(
                tuple(getattr(row, col) for col in df.columns)
            )
        except Exception as e:
            print(e)
            print(row)
            break
    
    cursor.executemany(query, values)

    conn.commit()

    cursor.close()


if __name__ == "__main__":
    conn = connect()
    conn2 = connect()

    insert_table(conn, 'empresa', QUERY_EMPRESA)
    insert_table(conn2, 'estabelecimento', QUERY_ESTABELECIMENTO)

    conn.close()
    conn2.close()