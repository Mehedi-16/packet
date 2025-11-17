import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))

with open("received.txt", 'wb') as f:
    while True:
        data, addr = server_socket.recvfrom(1024)
        if data == b'EOF':   # ফাইল শেষ signal
            break
        f.write(data)

print("File received successfully.")
server_socket.close()
