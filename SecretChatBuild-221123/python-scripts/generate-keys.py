from Crypto import Random
from Crypto.PublicKey import RSA
import base64

SECRET_KEY_BYTES_LENGNTH = 32
RSA_KEY_BITS_LENGNTH = 2048

def encode_base64(p):
    return base64.b64encode(p).decode('ascii')

secret = Random.get_random_bytes(SECRET_KEY_BYTES_LENGNTH)

rsa = RSA.generate(RSA_KEY_BITS_LENGNTH)
pubkey = rsa.publickey().exportKey()
prikey = rsa.exportKey()

print(encode_base64(secret) + '\n')

print(encode_base64(pubkey) + '\n')
print(encode_base64(prikey) + '\n')
