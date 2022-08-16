import os
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305

data = b"a secret message"
nonce = os.urandom(12)
key = ChaCha20Poly1305.generate_key()

def encrypt(msg, key):
    chacha = ChaCha20Poly1305(key)
    return chacha.encrypt(nonce, data, None)

def decrypt(msg, key):
    chacha = ChaCha20Poly1305(key)
    return chacha.decrypt(nonce, msg, None)

encrypted = encrypt(data, key)
print(f'Encryped: {str(encrypted)}')
print(f'Decrypted: {str(decrypt(encrypted, key))}')