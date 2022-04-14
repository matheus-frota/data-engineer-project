import os
import io
import shutil
import json

from dotenv import load_dotenv
from minio import Minio
from minio.error import S3Error
from numpy import r_
import pandas as pd

load_dotenv()


def create_temp(path_dir):
    if not os.path.isdir(path_dir):
        os.makedirs(path_dir)
    else:
        shutil.rmtree(path_dir)
        os.makedirs(path_dir)


def client():
    return Minio(
        "127.0.0.1:9000",
        access_key=os.getenv("MINIO_ACCESS_KEY"),
        secret_key=os.getenv("MINIO_SECRET_KEY"),
        secure=False
    )


def write_on_layer(filename, content, layer, route, bucket = 'roit', client = client()):
    try:
        if type(content) == pd.DataFrame:
            data = content.to_csv().encode('utf-8')
        else:
            data = str(content).encode('utf-8')
        client.put_object(f'{bucket}', f'{layer}/{route}/{filename}',
                            io.BytesIO(data), len(data), content_type='application/csv')
    except Exception as err:
        print(err)


def delete_on_layer(layer, route, bucket = 'roit', client = client()):
    try:
        objects = client.list_objects(bucket, prefix=f"{layer}/{route}", recursive=True)
        for obj in objects:
            client.remove_object(bucket, obj.object_name)
    except Exception as err:
        print(err)


def read_json_on_layer(layer, route, bucket = 'roit', client = client()):
    if not os.path.isdir('./roit-pipe/temp/'):
        os.makedirs('./roit-pipe/temp/')
    list_dfs = []
    objects = client.list_objects(bucket, prefix=f"{layer}/{route}", recursive=True)
    for i, complete_obj in enumerate(objects):
        try:
            filename = complete_obj.object_name.split('/')[2]
            obj = client.get_object(bucket, complete_obj.object_name)
            with open(f"./roit-pipe/temp/{filename}", 'wb') as f:
                for d in obj.stream(32*1024):
                    f.write(d)
            with open(f"./roit-pipe/temp/{filename}", 'rb') as f:
                t = str(f.read().decode())
                r = json.loads(t.replace("\'", "\""))
            df = pd.DataFrame([r])
            list_dfs.append(df)
        except Exception as err:
            continue
    frame = pd.concat(list_dfs)
    shutil.rmtree('./roit-pipe/temp/')
    return frame