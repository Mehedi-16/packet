import socket
import random

# UDP socket তৈরি
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12346))
print("Streaming Server ready...")

while True:
    # Client থেকে filename request
    data, addr = server_socket.recvfrom(1024)
    filename = data.decode()

    try:
        with open(filename, 'rb') as f:
            while True:
                # প্রতি বার random chunk (1000–2000 byte)
                chunk_size = random.randint(1000, 2000)
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                server_socket.sendto(chunk, addr)
    except FileNotFoundError:
        server_socket.sendto(b"File not found.", addr)
