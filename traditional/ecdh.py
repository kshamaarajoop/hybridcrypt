from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256

def generate_ecdh_keypair(curve='p256'):
    key=ECC.generate(curve=curve)
    return key,key.public_key()

def compute_shared_classical_secret(private_key,peer_public_key):
    shared_secret_point=private_key.d * peer_public_key.pointQ
    shared_secret=shared_secret_point.x.to_bytes()
    #optionally  to has for fixed length key
    return SHA256.new(shared_secret).digest()
    