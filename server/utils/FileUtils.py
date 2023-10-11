import hashlib


def get_md5(file):
    hash_object = hashlib.md5()
    for chunk in iter(lambda: file.read(), b""):
        hash_object.update(chunk)
    return hash_object.hexdigest()
