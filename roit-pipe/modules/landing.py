from uuid import uuid1

import requests

from io_minio import write_on_layer


def get(route, date):
    response = requests.get(f"http://localhost:8004/{route}/{date}")
    if response.status_code == 200:
        return response.json()
    return None


if __name__ == "__main__":
    responses = get("empresas", "2022-04-11")
    for r in responses:
        write_on_layer(f"{uuid1()}.json", r, "landing", "empresas")