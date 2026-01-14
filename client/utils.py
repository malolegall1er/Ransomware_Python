import os
import string

def generate_key(length=16):
    raw = os.urandom(2048)
    uppercase_letters = string.ascii_uppercase
    filtered = [chr(b) for b in raw if chr(b) in uppercase_letters]
    while len(filtered) < length:
        filtered += [chr(b) for b in os.urandom(512) if chr(b) in uppercase_letters]
    return ''.join(filtered[:length])

def get_machine_uuid():
    try:
        with open("/proc/sys/kernel/random/uuid", "r") as f:
            return f.read().strip()
    except Exception:
        return None
