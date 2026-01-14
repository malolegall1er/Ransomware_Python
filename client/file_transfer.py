import base64
import os

def upload_file(filepath):
    if not os.path.exists(filepath):
        return None, None
    try:
        with open(filepath, 'rb') as f:
            content = f.read()
        encoded = base64.b64encode(content).decode()
        filename = os.path.basename(filepath)
        return filename, encoded
    except Exception:
        return None, None
