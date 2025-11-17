import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server listening...")
conn, addr = server_socket.accept()
print("Connected by", addr)

with open("received_tcp.txt", 'wb') as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)
        # acknowledgment পাঠানো
        conn.sendall(b'ACK')

print("File received successfully (TCP).")
conn.close()
server_socket.close()
