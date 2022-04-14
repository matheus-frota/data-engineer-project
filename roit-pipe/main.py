from modules.io_minio import write_on_layer, read_json_on_layer, delete_on_layer
from modules.landing_raw import ingest_landing, ingest_raw
from modules.raw_trusted import ingest_trusted_empresas



def run_pipeline(route):
    print(route)
    print('Ingestão na landing...')
    ingest_landing(route, "2022-04-11")
    print('Ingestão na raw')
    ingest_raw(route)
    print('Ingestão na camada trusted')
    if route == 'empresas':
        ingest_trusted_empresas(route)
    elif route == 'estabelecimentos':
        pass


if __name__ == '__main__':
    for route in ['empresas', 'estabelecimentos']:
        run_pipeline(route)

