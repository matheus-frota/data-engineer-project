from uuid import uuid1

import requests

from io_minio import write_on_layer, read_json_on_layer, delete_on_layer


def get(route, date):
    response = requests.get(f"http://localhost:8004/{route}/{date}")
    if response.status_code == 200:
        return response.json()
    return None


if __name__ == "__main__":
    delete_on_layer("landing", "empresas")
    responses = get("empresas", "2022-04-11")
    for i, r in enumerate(responses):
        write_on_layer(f"{uuid1()}.json", r, "landing", "empresas")
        if i in [1000, 5000, 10000, 15000, 20000]:
            print(i)
    df = read_json_on_layer("landing", "empresas")
    print(df.head())
    print(df.shape)
    write_on_layer(f"{uuid1()}.csv", df, "raw", "empresas")