import hashlib

def md5_encrypt(text):
    m5 = hashlib.md5()
    #TypeError: Unicode-objects must be encoded before hashing for python3
    m5.update(text.encode('utf-8'))
    value = m5.hexdigest()
    return value


print(md5_encrypt("zhangsan01"))


