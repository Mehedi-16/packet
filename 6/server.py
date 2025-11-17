import socket
import threading

HOST = '127.0.0.1'
PORT = 12346

def handle_client(conn, addr):
    print(f"Client connected: {addr}")
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break
            print(f"{addr}: {msg}")

            reply = input("Server: ")
            conn.send(reply.encode())
        except:
            break
    print(f"Client disconnected: {addr}")
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server running on {HOST}:{PORT}")

try:
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
    
except KeyboardInterrupt:
    print("Server stopped")

server.close()
