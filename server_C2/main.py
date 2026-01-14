import threading
from init_server import start_init_server
from command_server import start_command_server

def main():
    threading.Thread(target=start_init_server, daemon=True).start()
    start_command_server()

if __name__ == "__main__":
    main()

