import hashlib


def get_md5(text: str):
    encode_text = text.encode("utf-8")
    md_ = hashlib.md5(encode_text)
    return md_.hexdigest()


if __name__ == '__main__':
    print(get_md5("learn-duck"))
