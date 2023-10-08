import os
import hashlib

def calc_hash(file_path):
    h = hashlib.sha256()
    with open(file_path, "rb") as fp:
        while True:
            data = fp.read(4096)
            if data == b"":
                break
            h.update(data)

    return h

def print_hashes(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.islink(file_path):
            continue
        if not os.path.isfile(file_path):
            continue

        h = calc_hash(file_path)
        print (f"{h.hexdigest()} {file}")

print_hashes(".")
