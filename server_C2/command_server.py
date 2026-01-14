import socket
from handler import handle_command_client

def start_command_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 9002))
    s.listen()
    print("[*] Serveur de commandes en écoute sur 9002")

    while True:
        conn, addr = s.accept()
        handle_command_client(conn, addr)
