import os
import io

from dotenv import load_dotenv
from minio import Minio
from minio.error import S3Error

load_dotenv()

def client():
    return Minio(
        "127.0.0.1:9000",
        access_key=os.getenv("MINIO_ACCESS_KEY"),
        secret_key=os.getenv("MINIO_SECRET_KEY"),
        secure=False
    )


def write_on_layer(filename, content, layer, route, bucket = 'roit', client = client()):
    try:
        data = str(content).encode('utf-8')
        client.put_object(f'{bucket}', f'{layer}/{route}/{filename}',
                            io.BytesIO(data), len(data), content_type='application/csv')
    except S3Error as err:
        print(err)


def delete_on_layer(layer, route, bucket = 'roit', client = client()):
    try:
        objects = client.list_objects(bucket, prefix=f"{layer}/{route}", recursive=True)
        for obj in objects:
            print(obj.object_name)
            client.remove_object(bucket, obj.object_name)
    except S3Error as err:
        print(err)