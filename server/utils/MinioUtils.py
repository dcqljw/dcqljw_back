from fastapi import UploadFile
from minio import Minio
from utils.FileUtils import get_md5
import Config


def main():
    client = Minio(
        Config.MINIO_ENDPOINT,
        access_key=Config.MINIO_ACCESS_KEY,
        secret_key=Config.MINIO_SECRET_KEY,
        secure=False
    )
    return client


def upload_file(buckets_name: str, file: UploadFile):
    try:
        client = main()
        client.put_object(buckets_name, file.filename, file.file, file.size, content_type=file.content_type)
        return fr"http://{Config.MINIO_ENDPOINT}/{buckets_name}/{file.filename}"
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
