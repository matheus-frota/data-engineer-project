from uuid import uuid1

import pandas as pd

from modules.io_minio import write_on_layer, read_json_on_layer, delete_on_layer


def ingest_trusted_empresas(route):
    df = read_json_on_layer("raw", route)
    df = df.drop_duplicates(['cnpj_basico'])
    write_on_layer(f"{uuid1()}.csv", df, "trusted", route)


if __name__ == '__main__':
    if route == "empresas":
        df = read_json_on_layer("raw", "empresas")
        df = df.drop_duplicates(['cnpj_basico'])
        write_on_layer(f"{uuid1()}.csv", df, "trusted", "empresas")
    else:
        pass