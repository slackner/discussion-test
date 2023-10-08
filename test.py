import os
import hashlib

def print_hashes(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.islink(file_path):
            continue
        if not os.path.isfile(file_path):
            continue

        def calc_hash(file_path):
            h = hashlib.md5()
            with open(file_path, "rb") as fp:
                while True:
                    data = fp.read(4096)
                    if not data:
                        break
                    h.update(data)

            return h

        h = calc_hash(file_path)
        print (f"{h.hexdigest()} {file}")

print_hashes(".")
