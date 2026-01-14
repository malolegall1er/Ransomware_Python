import socket
import threading
from handler import handle_init_client

def start_init_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 9001))
    s.listen()
    print("[*] Serveur INIT en écoute sur 9001 (UUID + clé)")

    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_init_client, args=(conn, addr)).start()
