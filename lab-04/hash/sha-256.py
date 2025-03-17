import hashlib

def caculate_sha256(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()
data_to_hash = input("Nhập dữ liệu cần băm: ")
sha256_value = caculate_sha256(data_to_hash)
print("Giá trị băm SHA-256 của dữ liệu '{}' là: {}".format(data_to_hash, sha256_value))