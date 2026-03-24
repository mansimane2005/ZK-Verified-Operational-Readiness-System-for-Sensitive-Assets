import hashlib


def generate_hash(file_path):

    sha = hashlib.sha256()

    with open(file_path, "rb") as f:
        while True:
            data = f.read(65536)

            if not data:
                break

            sha.update(data)

    return sha.hexdigest()
if __name__ == "__main__":

    h = generate_hash("onnx/model.onnx")

    print("Model Hash:")
    print(h)