# coding=utf-8

def main_handler(event, context):
    from Crypto.Hash import SHA256
    hash = SHA256.new()
    hash.update('message'.encode("utf-8"))
    print(hash.digest())   #'\xabS\n\x13\xe4Y\x14\x98+y\xf9\xb7\xe3\xfb\xa9\x94\xcf\xd1\xf3\xfb"\xf7\x1c\xea\x1a\xfb\xf0+F\x0cm\x1d'

    from Crypto.Cipher import AES
    obj = AES.new('This is a key123'.encode("utf-8"), AES.MODE_CBC, 'This is an IV456'.encode("utf-8"))
    message = "The answer is no".encode("utf-8")
    ciphertext = obj.encrypt(message)
    print(ciphertext) # '\xd6\x83\x8dd!VT\x92\xaa`A\x05\xe0\x9b\x8b\xf1'
    obj2 = AES.new('This is a key123'.encode("utf-8"), AES.MODE_CBC, 'This is an IV456'.encode("utf-8"))
    print(obj2.decrypt(ciphertext))  #'The answer is no'

    from Crypto import Random
    rndfile = Random.new()
    print(rndfile.read(16)) #'\xf7.\x838{\x85\xa0\xd3>#}\xc6\xc2jJU'


    resp = "test finish"
    return resp

